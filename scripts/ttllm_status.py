#!/usr/bin/env python3
"""Print free-core project status JSON (and optional site snapshot)."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from free_core.status import collect_status, status_json  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-site", action="store_true", help="Write site/demo/status_snapshot.json")
    ap.add_argument("--quiet-ok", action="store_true", help="Exit 1 if seal not verify+fresh")
    args = ap.parse_args()
    st = collect_status(REPO)
    text = status_json(REPO)
    print(text, end="")
    if args.write_site:
        out = REPO / "site" / "demo" / "status_snapshot.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        # strip absolute repo path for public snapshot
        pub = dict(st)
        pub["repo"] = "daisychainrrr (public)"
        import json
        out.write_text(json.dumps(pub, indent=2) + "\n", encoding="utf-8")
        print("wrote", out, file=sys.stderr)
    if args.quiet_ok:
        seal = st.get("seal") or {}
        if not (seal.get("verify_ok") and seal.get("fresh")):
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
