#!/usr/bin/env python3
"""Train nano-v2 on BPE tokens with dense checkpoints + val perplexity."""
from __future__ import annotations
import argparse, array, json, math, time, sys
from datetime import datetime, timezone
from pathlib import Path
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from model import NanoGPT


def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps", type=int, default=1500)
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--block-size", type=int, default=128)
    ap.add_argument("--n-layer", type=int, default=6)
    ap.add_argument("--n-head", type=int, default=4)
    ap.add_argument("--n-embd", type=int, default=192)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--ckpt-every", type=int, default=150)
    ap.add_argument("--eval-every", type=int, default=50)
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()

    torch.manual_seed(args.seed)
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print("device", device)

    meta = json.loads((ROOT / "data/processed/meta_v2.json").read_text())
    raw = (ROOT / "data/processed/tokens.bin").read_bytes()
    arr = array.array("I")
    arr.frombytes(raw)
    data = torch.tensor(arr.tolist(), dtype=torch.long)
    n = int(0.9 * len(data))
    train_data, val_data = data[:n], data[n:]
    print("tokens", len(data), "train", len(train_data), "val", len(val_data), "vocab", meta["vocab_size"])

    def get_batch(split):
        src = train_data if split == "train" else val_data
        ix = torch.randint(len(src) - args.block_size - 1, (args.batch_size,))
        x = torch.stack([src[i : i + args.block_size] for i in ix])
        y = torch.stack([src[i + 1 : i + args.block_size + 1] for i in ix])
        return x.to(device), y.to(device)

    model = NanoGPT(
        vocab_size=meta["vocab_size"],
        block_size=args.block_size,
        n_layer=args.n_layer,
        n_head=args.n_head,
        n_embd=args.n_embd,
    ).to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr)
    n_params = sum(p.numel() for p in model.parameters())
    print("params", n_params)

    ckpt_dir = ROOT / "checkpoints"
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    metrics_path = ROOT / "metrics" / "train.jsonl"
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text("")

    hyper = {
        "schema": "ttllm.nano.v2.hyperparams",
        "version": "0.2.0-nano-bpe",
        "steps": args.steps,
        "batch_size": args.batch_size,
        "block_size": args.block_size,
        "n_layer": args.n_layer,
        "n_head": args.n_head,
        "n_embd": args.n_embd,
        "lr": args.lr,
        "seed": args.seed,
        "device": device,
        "n_params": n_params,
        "tokenizer": "bpe-utf8-base",
        "vocab_size": meta["vocab_size"],
        "corpus_sha256": meta["corpus_sha256"],
        "tokens_sha256": meta["tokens_sha256"],
        "started_utc": utc(),
    }
    (ROOT / "metrics" / "hyperparams.json").write_text(json.dumps(hyper, indent=2) + "\n")

    def save_ckpt(step, val_loss):
        path = ckpt_dir / f"step_{step:06d}.pt"
        torch.save({
            "step": step,
            "model": model.state_dict(),
            "optimizer": opt.state_dict(),
            "hyper": hyper,
            "val_loss": val_loss,
            "saved_utc": utc(),
        }, path)
        print("ckpt", path.name, "val_loss", val_loss)

    @torch.no_grad()
    def estimate_loss():
        model.eval()
        out = {}
        for split in ("train", "val"):
            vals = []
            for _ in range(20):
                xb, yb = get_batch(split)
                _, loss = model(xb, yb)
                vals.append(loss.item())
            out[split] = sum(vals) / len(vals)
            out[f"{split}_ppl"] = math.exp(min(out[split], 20))
        model.train()
        return out

    t0 = time.time()
    save_ckpt(0, None)
    model.train()
    for step in range(1, args.steps + 1):
        xb, yb = get_batch("train")
        _, loss = model(xb, yb)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        if step % args.eval_every == 0 or step == 1:
            losses = estimate_loss()
            row = {
                "step": step,
                "train_loss": losses["train"],
                "val_loss": losses["val"],
                "val_ppl": losses["val_ppl"],
                "wall_sec": time.time() - t0,
                "utc": utc(),
            }
            with metrics_path.open("a") as f:
                f.write(json.dumps(row) + "\n")
            print(f"step {step} train {losses['train']:.4f} val {losses['val']:.4f} ppl {losses['val_ppl']:.2f}")
        if step % args.ckpt_every == 0 or step == args.steps:
            losses = estimate_loss()
            save_ckpt(step, losses["val"])

    torch.save({"step": args.steps, "model": model.state_dict(), "hyper": hyper, "saved_utc": utc()}, ckpt_dir / "final.pt")
    hyper["finished_utc"] = utc()
    hyper["wall_sec"] = time.time() - t0
    (ROOT / "metrics" / "hyperparams.json").write_text(json.dumps(hyper, indent=2) + "\n")
    print("done wall", hyper["wall_sec"])


if __name__ == "__main__":
    main()
