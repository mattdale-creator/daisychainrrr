#!/usr/bin/env python3
"""Emit evidence-based master domain scorecard (Domains 1–10)."""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.org.domain_scorecard import write_master_scorecard  # noqa: E402


def main() -> int:
    out, card = write_master_scorecard(REPO)
    print("wrote", out)
    print(
        json.dumps(
            {
                "domains": len(card["domains"]),
                "statuses": {d["number"]: d["status"] for d in card["domains"]},
                "artefact_md_count": card.get("artefact_md_count"),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
