"""Merkle inclusion proofs for TTLLM manifests."""
from __future__ import annotations
import hashlib
from typing import List, Optional, Tuple, Dict, Any


def _pair_hash(left: bytes, right: bytes) -> bytes:
    return hashlib.sha256(left + right).digest()


def build_tree_levels(leaf_hex: List[str]) -> List[List[bytes]]:
    if not leaf_hex:
        return []
    level = [bytes.fromhex(d) for d in leaf_hex]
    levels = [level]
    while len(level) > 1:
        nxt = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else left
            nxt.append(_pair_hash(left, right))
        level = nxt
        levels.append(level)
    return levels


def inclusion_proof(leaf_hex: List[str], index: int) -> Dict[str, Any]:
    """Return proof siblings from leaf to root for leaf at index."""
    if index < 0 or index >= len(leaf_hex):
        raise IndexError("leaf index out of range")
    levels = build_tree_levels(leaf_hex)
    proof = []
    idx = index
    for level in levels[:-1]:
        if len(level) == 1:
            break
        if idx % 2 == 0:
            sib_i = idx + 1 if idx + 1 < len(level) else idx
            position = "right"
        else:
            sib_i = idx - 1
            position = "left"
        proof.append({"position": position, "hash": level[sib_i].hex()})
        idx //= 2
    root = levels[-1][0].hex() if levels else None
    return {
        "schema": "ttllm.merkle_proof.v1",
        "leaf_index": index,
        "leaf_hash": leaf_hex[index],
        "proof": proof,
        "root": root,
    }


def verify_inclusion(leaf_hash_hex: str, proof: List[dict], expected_root: str) -> bool:
    cur = bytes.fromhex(leaf_hash_hex)
    for step in proof:
        sib = bytes.fromhex(step["hash"])
        if step["position"] == "left":
            cur = _pair_hash(sib, cur)
        else:
            cur = _pair_hash(cur, sib)
    return cur.hex() == expected_root
