"""Minimal byte-pair encoding for nano-v2 — pure Python, no external tokenizers."""
from __future__ import annotations
import json
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple


def get_stats(ids: List[int]) -> Counter:
    pairs = Counter()
    for i in range(len(ids) - 1):
        pairs[(ids[i], ids[i + 1])] += 1
    return pairs


def merge(ids: List[int], pair: Tuple[int, int], new_id: int) -> List[int]:
    out = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i + 1] == pair[1]:
            out.append(new_id)
            i += 2
        else:
            out.append(ids[i])
            i += 1
    return out


def train_bpe(text: str, num_merges: int = 500) -> dict:
    # start with bytes 0-255 as base vocab for UTF-8
    raw = list(text.encode("utf-8"))
    merges: List[Tuple[int, int]] = []
    vocab_size = 256
    ids = raw[:]
    for _ in range(num_merges):
        stats = get_stats(ids)
        if not stats:
            break
        pair = max(stats, key=stats.get)
        if stats[pair] < 2:
            break
        new_id = vocab_size
        vocab_size += 1
        ids = merge(ids, pair, new_id)
        merges.append(pair)
    return {
        "schema": "ttllm.nano.bpe.v1",
        "base": 256,
        "vocab_size": vocab_size,
        "merges": [[a, b] for a, b in merges],
        "num_merges": len(merges),
    }


def encode(text: str, merges: List[Tuple[int, int]]) -> List[int]:
    ids = list(text.encode("utf-8"))
    for i, pair in enumerate(merges):
        new_id = 256 + i
        ids = merge(ids, pair, new_id)
    return ids


def decode(ids: List[int], merges: List[Tuple[int, int]]) -> str:
    # reverse merges
    pairs = list(enumerate(merges))
    for i, pair in reversed(pairs):
        new_id = 256 + i
        out = []
        for tok in ids:
            if tok == new_id:
                out.extend(pair)
            else:
                out.append(tok)
        ids = out
    return bytes(ids).decode("utf-8", errors="replace")


def save(obj: dict, path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
