#!/usr/bin/env python3
"""Run the automated half of the company testing loop (phases 3 + red-team suite).

Normative procedure: docs/security/TESTING_LOOP.md
First cycle record: docs/audits/loops/LOOP_2026-08-08.md

Does NOT claim SoT reload / soft-tissue prose / new campaign design are done —
those remain interactive. Exit 0 only if all automated checks pass.
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def _run(label: str, cmd: list[str]) -> int:
    print(f"\n=== {label} ===", flush=True)
    print("+", " ".join(cmd), flush=True)
    return subprocess.call(cmd, cwd=str(REPO))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="TTLLM testing-loop automated suite")
    ap.add_argument(
        "--with-network",
        action="store_true",
        help="Also run public URL + DNS probes (ttllms.org may fail T1 — non-fatal unless --strict-network)",
    )
    ap.add_argument(
        "--strict-network",
        action="store_true",
        help="Fail if network probes fail (default: record only; org DNS is hard gate T1)",
    )
    ap.add_argument(
        "--record",
        action="store_true",
        help="Write registers/redteam/last_testing_loop_run.json summary",
    )
    ap.add_argument(
        "--skip-business",
        action="store_true",
        help="Skip redteam_business_attack.py (integrity suite only)",
    )
    args = ap.parse_args(argv)

    py = sys.executable
    results: dict[str, int] = {}
    fails: list[str] = []

    steps = [
        ("oneshot_verify_all", [py, "scripts/oneshot_verify_all.py"]),
        ("pytest", [py, "-m", "pytest", "-q"]),
        ("redteam_nano_harness", [py, "scripts/redteam_nano_harness.py"]),
    ]
    if not args.skip_business:
        steps.append(("redteam_business_attack", [py, "scripts/redteam_business_attack.py"]))
    steps.append(("ttllm_status_quiet_ok", [py, "scripts/ttllm_status.py", "--quiet-ok"]))

    for label, cmd in steps:
        code = _run(label, cmd)
        results[label] = code
        if code != 0:
            fails.append(label)

    network: dict[str, int] = {}
    if args.with_network:
        for label, script in (
            ("check_public_urls", "check_public_urls.py"),
            ("check_dns_status", "check_dns_status.py"),
        ):
            code = _run(label, [py, f"scripts/{script}"])
            network[label] = code
            results[label] = code
            if args.strict_network and code != 0:
                fails.append(label)

    utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    summary = {
        "schema": "ttllm.testing_loop_run.v1",
        "utc": utc,
        "ethos": "Measure twice. Attack the skeleton. Publish the red. Never fake the green.",
        "procedure": "docs/security/TESTING_LOOP.md",
        "first_cycle_record": "docs/audits/loops/LOOP_2026-08-08.md",
        "results": results,
        "network": network or None,
        "fails": fails,
        "ok": len(fails) == 0,
        "human_phases_remaining": [
            "reload_founding_SoT",
            "soft_tissue_triple_check",
            "fix_agent_fixable",
            "new_campaign_if_cadence_requires",
            "file_LOOP_YYYY-MM-DD",
        ],
    }
    print("\n=== testing_loop summary ===")
    print(json.dumps(summary, indent=2))

    if args.record or True:
        out = REPO / "registers" / "redteam" / "last_testing_loop_run.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out}", file=sys.stderr)

    if fails:
        print("TESTING_LOOP_AUTOMATED: FAIL", fails, file=sys.stderr)
        return 1
    print("TESTING_LOOP_AUTOMATED: PASS (human phases still required for full loop)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
