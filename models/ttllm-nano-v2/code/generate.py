#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import torch
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from model import NanoGPT
from bpe import load, encode, decode

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", default=str(ROOT / "checkpoints/final.pt"))
    ap.add_argument("--prompt", default="Alice ")
    ap.add_argument("--tokens", type=int, default=150)
    ap.add_argument("--temperature", type=float, default=0.9)
    args = ap.parse_args()
    bpe = load(ROOT / "data/processed/bpe.json")
    merges = [tuple(p) for p in bpe["merges"]]
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    blob = torch.load(args.ckpt, map_location=device, weights_only=False)
    h = blob["hyper"]
    model = NanoGPT(h["vocab_size"], h["block_size"], h["n_layer"], h["n_head"], h["n_embd"]).to(device)
    model.load_state_dict(blob["model"])
    model.eval()
    ids = encode(args.prompt, merges)
    idx = torch.tensor([ids], dtype=torch.long, device=device)
    with torch.no_grad():
        for _ in range(args.tokens):
            cond = idx[:, -h["block_size"]:]
            logits, _ = model(cond)
            logits = logits[:, -1, :] / max(args.temperature, 1e-6)
            probs = torch.softmax(logits, dim=-1)
            nxt = torch.multinomial(probs, 1)
            idx = torch.cat([idx, nxt], dim=1)
    print(decode(idx[0].tolist(), merges))

if __name__ == "__main__":
    main()
