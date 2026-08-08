#!/usr/bin/env python3
"""Probe DNS honesty for ttllms.com / .org — no secrets, no fake Active."""
from __future__ import annotations
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NAMES = [
    ("ttllms.com", True),
    ("www.ttllms.com", True),
    ("ttllms.org", False),
    ("www.ttllms.org", False),
    ("ttllms.pages.dev", True),
]


def dig(name: str, rtype: str) -> list[str]:
    if not shutil.which("dig"):
        return []
    try:
        out = subprocess.check_output(
            ["dig", "+short", rtype, name],
            text=True,
            timeout=15,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return []
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def probe(name: str) -> dict:
    cname = dig(name, "CNAME")
    a = dig(name, "A")
    aaaa = dig(name, "AAAA")
    ns = dig(name, "NS")
    has_addr = bool(cname or a or aaaa)
    return {
        "name": name,
        "cname": cname,
        "a": a,
        "aaaa": aaaa,
        "ns": ns,
        "resolves": has_addr,
    }


def main() -> int:
    rows = [probe(n) for n, _ in NAMES]
    required_ok = all(probe(n)["resolves"] for n, req in NAMES if req)
    optional_fail = [n for n, req in NAMES if not req and not probe(n)["resolves"]]
    report = {
        "schema": "ttllm.dns_status.v1",
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "required_ok": required_ok,
        "optional_unresolved": optional_fail,
        "rows": rows,
        "human_gate": "docs/handbook/gates/01-dns-org.md" if optional_fail else None,
    }
    out = REPO / "ops" / "last_dns_status.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    for r in rows:
        flag = "OK" if r["resolves"] else "FAIL"
        print(f"{flag} {r['name']} cname={r['cname'][:1] or '-'} a={len(r['a'])}")
    # required fail => exit 1; org optional
    return 0 if required_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
