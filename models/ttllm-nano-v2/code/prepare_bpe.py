#!/usr/bin/env python3
"""Train BPE on existing PG corpus and write token ids."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from bpe import train_bpe, encode, save

ROOT = Path(__file__).resolve().parents[1]
corpus_path = ROOT / "data/processed/corpus.txt"
if not corpus_path.exists():
    raise SystemExit("missing corpus — run nano v1 prepare_data first or rsync data")

text = corpus_path.read_text(encoding="utf-8")
print("training BPE on", len(text), "chars…")
bpe = train_bpe(text, num_merges=800)
merges = [tuple(p) for p in bpe["merges"]]
ids = encode(text, merges)
print("vocab", bpe["vocab_size"], "tokens", len(ids))

proc = ROOT / "data/processed"
save(bpe, proc / "bpe.json")
# store as binary int32-ish json list in chunks is huge — use raw bytes of uint16
import array
arr = array.array("I", ids)
(proc / "tokens.bin").write_bytes(arr.tobytes())
meta = {
    "schema": "ttllm.nano.v2.meta",
    "vocab_size": bpe["vocab_size"],
    "n_tokens": len(ids),
    "corpus_sha256": hashlib.sha256(text.encode()).hexdigest(),
    "tokens_sha256": hashlib.sha256(arr.tobytes()).hexdigest(),
    "bpe_merges": len(merges),
}
(proc / "meta_v2.json").write_text(json.dumps(meta, indent=2) + "\n")
print("wrote tokens.bin", len(arr.tobytes()), "bytes")
