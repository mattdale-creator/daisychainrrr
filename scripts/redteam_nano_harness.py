#!/usr/bin/env python3
"""Minimal adversarial harness against transparency layer (founding turn 14–16)."""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.provenance.manifest import load_manifest, verify_manifest, build_merkle_manifest, write_manifest
from free_core.stream.log import StreamLog
from free_core.security.query_guard import QueryGuard


def main():
    results = []
    # 1) tamper detection on a temp manifest of examples
    ex = list((REPO / "examples" / "corpus").glob("*.txt"))
    if ex:
        man = build_merkle_manifest(ex, base=REPO)
        # verify ok
        ok1 = verify_manifest(man, REPO)["ok"]
        # tamper file content in memory check: change leaf
        man2 = json.loads(json.dumps(man))
        man2["leaves"][0]["sha256"] = "0" * 64
        from free_core.provenance.manifest import merkle_root
        # verify should fail vs files
        ok2 = verify_manifest(man2, REPO)["ok"]
        results.append({"test": "manifest_tamper_detected", "pass": ok1 and (ok2 is False)})
    # 2) stream chain break detection
    log = StreamLog()
    from free_core.stream.schema import StreamEvent
    log.append(StreamEvent(event_type="a", payload={"n": 1}))
    log.append(StreamEvent(event_type="b", payload={"n": 2}))
    ok_chain = log.verify_chain()["ok"]
    log.events[1]["payload"]["n"] = 99
    broken = log.verify_chain()["ok"] is False
    results.append({"test": "stream_tamper_detected", "pass": ok_chain and broken})
    # 3) query guard
    g = QueryGuard(hard_limit=3)
    allowed = sum(1 for _ in range(3) if g.allow("x"))
    blocked = g.allow("x") is False
    results.append({"test": "query_guard_rate_limit", "pass": allowed == 3 and blocked})

    out = {"schema": "ttllm.redteam_harness.v1", "results": results, "all_pass": all(r["pass"] for r in results)}
    path = REPO / "registers" / "redteam" / "last_harness_run.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    sys.exit(0 if out["all_pass"] else 1)


if __name__ == "__main__":
    main()
