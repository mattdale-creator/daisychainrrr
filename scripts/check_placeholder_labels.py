#!/usr/bin/env python3
"""Ensure docs/placeholders/** carry the Grok human-check label."""
from __future__ import annotations
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LABEL = "Written by Grok - Human checking required"
ROOT = REPO / "docs" / "placeholders"


def main() -> int:
    if not ROOT.is_dir():
        print("MISSING", ROOT)
        return 1
    fails = []
    files = list(ROOT.rglob("*.md"))
    for p in files:
        if p.name == "BANNER.md":
            continue
        text = p.read_text(encoding="utf-8")
        if LABEL not in text:
            fails.append(str(p.relative_to(REPO)))
    print("checked", len(files), "fails", len(fails))
    for f in fails:
        print("MISSING_LABEL", f)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
