#!/usr/bin/env python3
"""Publish verified multi-nano stream tips to the public site.

Free public core — offline, unpaid. Re-verifies each hash chain before write.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.stream.nano_tips import write_nano_stream_tips  # noqa: E402


def main() -> int:
    tips = write_nano_stream_tips(REPO, copy_logs=True)
    summary = {
        "all_chain_ok": tips["all_chain_ok"],
        "nano_count": tips["nano_count"],
        "wrote": tips.get("wrote"),
        "tips": [
            {
                "name": n["name"],
                "chain_ok": n.get("chain_ok"),
                "count": n.get("count"),
                "tip": (n.get("tip") or "")[:16] + "…" if n.get("tip") else None,
            }
            for n in tips.get("nanos", [])
        ],
    }
    print(json.dumps(summary, indent=2))
    return 0 if tips["all_chain_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
