"""Canary documents for ttlink index poisoning detection."""
from __future__ import annotations
import json
from pathlib import Path
from free_core.provenance.hashing import sha256_bytes
from free_core.ttlink.index import TtlinkIndex


CANARY_PREFIX = "TTLLM_CANARY_UNIQUE_"


def make_canary(secret: str = "bone-not-soft-tissue") -> dict:
    text = f"{CANARY_PREFIX}{secret}\nThis line must never appear in training data.\n"
    return {
        "doc_id": f"canary_{sha256_bytes(secret.encode())[:12]}",
        "text": text,
        "sha256": sha256_bytes(text.encode()),
    }


def inject_canary(index: TtlinkIndex, secret: str = "bone-not-soft-tissue") -> dict:
    c = make_canary(secret)
    index.add_document(c["doc_id"], c["text"], path=f"canary/{c['doc_id']}.txt")
    return c


def check_canary(index: TtlinkIndex, secret: str = "bone-not-soft-tissue") -> dict:
    c = make_canary(secret)
    span = CANARY_PREFIX + secret
    hits = index.query(span)
    ok = any(h.doc_sha256 == c["sha256"] for h in hits)
    return {"ok": ok, "hits": len(hits), "expected_sha256": c["sha256"]}
