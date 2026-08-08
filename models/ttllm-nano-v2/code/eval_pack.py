#!/usr/bin/env python3
"""Stronger eval pack: val loss/ppl from metrics + ttlink retrieval + BPE roundtrip."""
from __future__ import annotations
import json, sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(ROOT / "code"))
from bpe import load, encode, decode
from free_core.ttlink.index import TtlinkIndex


def main():
    metrics = []
    mp = ROOT / "metrics/train.jsonl"
    if mp.exists():
        for line in mp.read_text().splitlines():
            if line.strip():
                metrics.append(json.loads(line))
    last = metrics[-1] if metrics else {}
    bpe = load(ROOT / "data/processed/bpe.json")
    merges = [tuple(p) for p in bpe["merges"]]
    samples = ["Alice ", "Elizabeth", "Frankenstein", "the ", "\n"]
    roundtrip_ok = 0
    for s in samples:
        if decode(encode(s, merges), merges) == s:
            roundtrip_ok += 1
    # ttlink
    idx = TtlinkIndex()
    for p in sorted((ROOT / "data/raw").glob("*.trainslice.txt")):
        idx.add_file(p, doc_id=p.name)
    retrieval = {q: len(idx.query(q, max_hits=5)) for q in ["Alice", "Darcy", "monster", "Gutenberg"]}
    pack = {
        "schema": "ttllm.nano.v2.eval.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "final_metrics": last,
        "bpe_roundtrip": {"n": len(samples), "ok": roundtrip_ok, "pass": roundtrip_ok == len(samples)},
        "ttlink_retrieval_hits": retrieval,
        "honesty": "No frontier capability claims. Eval proves process: metrics exist, BPE invertible on samples, ttlink finds corpus spans.",
    }
    out = ROOT / "evals/eval_pack.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(pack, indent=2) + "\n")
    print(json.dumps(pack, indent=2))
    return 0 if pack["bpe_roundtrip"]["pass"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
