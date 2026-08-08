#!/usr/bin/env python3
"""Print free-core project status JSON (and optional site snapshot)."""
from __future__ import annotations
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from free_core.status import main as status_main  # noqa: E402


def main() -> int:
    # Force repo root when invoked as scripts/ttllm_status.py
    argv = list(sys.argv[1:])
    if "--repo" not in argv:
        argv = ["--repo", str(REPO), *argv]
    return status_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
