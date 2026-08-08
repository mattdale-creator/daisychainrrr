#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from model import NanoGPT


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", default=str(ROOT / "checkpoints/final.pt"))
    ap.add_argument("--prompt", default="Alice ")
    ap.add_argument("--tokens", type=int, default=200)
    ap.add_argument("--temperature", type=float, default=0.8)
    args = ap.parse_args()
    meta = json.loads((ROOT / "data/processed/meta.json").read_text())
    stoi, itos = meta["stoi"], {int(k): v for k, v in meta["itos"].items()}
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    blob = torch.load(args.ckpt, map_location=device, weights_only=False)
    h = blob["hyper"]
    model = NanoGPT(meta["vocab_size"], h["block_size"], h["n_layer"], h["n_head"], h["n_embd"]).to(device)
    model.load_state_dict(blob["model"])
    model.eval()
    idx = torch.tensor([[stoi.get(c, 0) for c in args.prompt]], dtype=torch.long, device=device)
    out = model.generate(idx, args.tokens, temperature=args.temperature)[0].tolist()
    print("".join(itos[i] for i in out))


if __name__ == "__main__":
    main()
