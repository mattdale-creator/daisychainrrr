#!/usr/bin/env python3
"""Continuous bone-level build driver. Idempotent tasks; exit 0 always so outer loop continues."""
from __future__ import annotations
import json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LEDGER = REPO / "docs/audits/WORK_LEDGER.md"
STATE = REPO / "docs/audits/CONTINUOUS_LOOP_STATE.json"

def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def log(msg: str):
    line = f"| {utc()[:10]} | continuous | {msg} |\n"
    with LEDGER.open("a") as f:
        f.write(line)
    print(msg, flush=True)

def run(cmd, timeout=600):
    print("+", " ".join(cmd), flush=True)
    return subprocess.run(cmd, cwd=REPO, timeout=timeout)

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"iteration": 0, "completed_tasks": []}

def save_state(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    s["updated"] = utc()
    STATE.write_text(json.dumps(s, indent=2) + "\n")

def main():
    s = load_state()
    s["iteration"] = s.get("iteration", 0) + 1
    log(f"loop iteration {s['iteration']}")
    # always run tests
    r = run([sys.executable, "-m", "pytest", "-q"], timeout=120)
    s["last_pytest"] = r.returncode
    save_state(s)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
