#!/usr/bin/env python3
"""Train ttllm-nano with dense intermediate checkpoints + JSONL metrics.

Mac M1: prefers MPS, falls back to CPU.
"""
from __future__ import annotations
import argparse
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
import sys

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from model import NanoGPT  # noqa: E402


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps", type=int, default=800)
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--block-size", type=int, default=128)
    ap.add_argument("--n-layer", type=int, default=4)
    ap.add_argument("--n-head", type=int, default=4)
    ap.add_argument("--n-embd", type=int, default=128)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--ckpt-every", type=int, default=100)
    ap.add_argument("--eval-every", type=int, default=50)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    torch.manual_seed(args.seed)
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print("device", device)

    meta = json.loads((ROOT / "data/processed/meta.json").read_text())
    corpus = (ROOT / "data/processed/corpus.txt").read_text(encoding="utf-8")
    stoi = meta["stoi"]
    data = torch.tensor([stoi[c] for c in corpus], dtype=torch.long)
    n = int(0.9 * len(data))
    train_data, val_data = data[:n], data[n:]

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

    ckpt_dir = ROOT / "checkpoints"
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    metrics_path = ROOT / "metrics" / "train.jsonl"
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    # fresh metrics
    metrics_path.write_text("")

    hyper = {
        "schema": "ttllm.nano.hyperparams.v1",
        "steps": args.steps,
        "batch_size": args.batch_size,
        "block_size": args.block_size,
        "n_layer": args.n_layer,
        "n_head": args.n_head,
        "n_embd": args.n_embd,
        "lr": args.lr,
        "seed": args.seed,
        "device": device,
        "optimizer": "AdamW",
        "corpus_sha256": meta["corpus_sha256"],
        "vocab_size": meta["vocab_size"],
        "started_utc": utc(),
    }
    (ROOT / "metrics" / "hyperparams.json").write_text(json.dumps(hyper, indent=2) + "\n")

    # step 0 checkpoint
    def save_ckpt(step: int, val_loss: float | None):
        path = ckpt_dir / f"step_{step:06d}.pt"
        payload = {
            "step": step,
            "model": model.state_dict(),
            "optimizer": opt.state_dict(),
            "hyper": hyper,
            "val_loss": val_loss,
            "saved_utc": utc(),
        }
        torch.save(payload, path)
        print(f"ckpt {path} val_loss={val_loss}")

    @torch.no_grad()
    def estimate_loss():
        model.eval()
        losses = {}
        for split in ("train", "val"):
            vals = []
            for _ in range(10):
                xb, yb = get_batch(split)
                _, loss = model(xb, yb)
                vals.append(loss.item())
            losses[split] = sum(vals) / len(vals)
        model.train()
        return losses

    t0 = time.time()
    save_ckpt(0, None)
    model.train()
    for step in range(1, args.steps + 1):
        xb, yb = get_batch("train")
        _, loss = model(xb, yb)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()

        if step % args.eval_every == 0 or step == 1:
            losses = estimate_loss()
            row = {
                "step": step,
                "train_loss": losses["train"],
                "val_loss": losses["val"],
                "wall_sec": time.time() - t0,
                "utc": utc(),
            }
            with metrics_path.open("a") as f:
                f.write(json.dumps(row) + "\n")
            print(f"step {step} train {losses['train']:.4f} val {losses['val']:.4f}")

        if step % args.ckpt_every == 0 or step == args.steps:
            losses = estimate_loss()
            save_ckpt(step, losses["val"])

    # final
    final = ckpt_dir / "final.pt"
    torch.save({"step": args.steps, "model": model.state_dict(), "hyper": hyper, "saved_utc": utc()}, final)
    hyper["finished_utc"] = utc()
    hyper["wall_sec"] = time.time() - t0
    (ROOT / "metrics" / "hyperparams.json").write_text(json.dumps(hyper, indent=2) + "\n")
    print("done", final)


if __name__ == "__main__":
    main()
