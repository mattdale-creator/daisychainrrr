#!/usr/bin/env python3
"""Build synthetic incident stream example (clearly marked drill — not production incident)."""
from __future__ import annotations
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from free_core.stream.schema import StreamEvent  # noqa: E402
from free_core.stream.log import StreamLog  # noqa: E402

def main() -> int:
    log = StreamLog()
    log.append(StreamEvent(
        event_type="incident_drill",
        payload={
            "scenario": "Public Merkle root mismatches files after a bad deploy",
            "date": "2026-08-08",
            "register": "registers/incidents/TABLETOP_2026-08-08.md",
            "synthetic": True,
        },
    ))
    log.append(StreamEvent(
        event_type="incident_opened",
        payload={
            "incident_id": "DRILL-I-0001",
            "severity": "High",
            "category": "integrity",
            "summary": "SYNTHETIC drill: seal mismatch detection path",
            "synthetic": True,
        },
    ))
    log.append(StreamEvent(
        event_type="claim_tombstoned",
        payload={
            "claim": "FREE_CORE_SEAL green (drill)",
            "reason": "Simulated mismatch — tombstone until reseal",
            "synthetic": True,
        },
    ))
    log.append(StreamEvent(
        event_type="incident_mitigated",
        payload={
            "incident_id": "DRILL-I-0001",
            "action": "reseal from known-good commit (simulated)",
            "synthetic": True,
        },
    ))
    log.append(StreamEvent(
        event_type="incident_closed",
        payload={
            "incident_id": "DRILL-I-0001",
            "residual": "none — drill only",
            "synthetic": True,
        },
    ))
    out = REPO / "examples" / "stream" / "incident_drill_log.json"
    log.save(out)
    ch = log.verify_chain()
    print("wrote", out, ch)
    return 0 if ch.get("ok") else 1

if __name__ == "__main__":
    raise SystemExit(main())
