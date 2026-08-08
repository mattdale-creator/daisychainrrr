#!/usr/bin/env python3
"""Write docs/specs/artefacts/stream/STREAM_EVENT_CATALOG.md from free_core.stream.catalog."""
from __future__ import annotations
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from free_core.stream.catalog import catalog_markdown, EVENT_TYPES  # noqa: E402
import json

def main() -> int:
    out = REPO / "docs" / "specs" / "artefacts" / "stream" / "STREAM_EVENT_CATALOG.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(catalog_markdown(), encoding="utf-8")
    jpath = REPO / "free_core" / "schemas" / "stream_event_types.json"
    jpath.write_text(
        json.dumps({"schema": "ttllm.stream_event_types.v1", "types": EVENT_TYPES}, indent=2) + "\n",
        encoding="utf-8",
    )
    print("wrote", out)
    print("wrote", jpath)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
