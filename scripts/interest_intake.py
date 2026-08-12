#!/usr/bin/env python3
"""CLI: classify pre-revenue inbound interest (no invoices).

Examples:
  python3 scripts/interest_intake.py --demo
  python3 scripts/interest_intake.py --text "we want exclusive free-core weights"
  echo "hosted SLA please" | python3 scripts/interest_intake.py
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.business.interest_intake import (  # noqa: E402
    DEMO_MESSAGES,
    classify_batch,
    classify_interest,
    demo_corpus_ok,
)


def main() -> int:
    ap = argparse.ArgumentParser(description="TTLLM pre-revenue interest intake")
    ap.add_argument("--text", default=None, help="Single message body")
    ap.add_argument("--demo", action="store_true", help="Run fixed demo corpus")
    ap.add_argument(
        "--write-site",
        action="store_true",
        help="Write site/demo/interest_intake_demo.json",
    )
    args = ap.parse_args()

    if args.demo or args.write_site:
        messages = [t for t, _ in DEMO_MESSAGES]
        batch = classify_batch(messages)
        batch["demo_corpus_ok"] = demo_corpus_ok()
        # attach expected for transparency
        batch["demo_expected"] = [
            {"text": t[:120], "expected_path": e} for t, e in DEMO_MESSAGES
        ]
        print(json.dumps(batch, indent=2))
        if args.write_site:
            out = REPO / "site" / "demo" / "interest_intake_demo.json"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(batch, indent=2) + "\n", encoding="utf-8")
            print(f"wrote {out.relative_to(REPO)}", file=sys.stderr)
        return 0 if batch.get("demo_corpus_ok") else 1

    text = args.text
    if text is None:
        if not sys.stdin.isatty():
            text = sys.stdin.read()
        else:
            ap.error("provide --text, --demo, or pipe stdin")
    v = classify_interest(text)
    print(json.dumps(v.to_dict(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
