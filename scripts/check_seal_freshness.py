#!/usr/bin/env python3
"""Fail if FREE_CORE_SEAL.json is stale vs current free-core targets.

Ethos: green verify of a stale seal after soft-tissue edits is a lie.
Exit 0 = fresh (or --write just resealed). Exit 1 = stale.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.provenance.seal_targets import build_free_core_manifest  # noqa: E402
from free_core.provenance.manifest import load_manifest, write_manifest  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check FREE_CORE_SEAL freshness")
    ap.add_argument("--root", default=str(REPO))
    ap.add_argument("--manifest", default=None, help="Path to seal (default manifests/FREE_CORE_SEAL.json)")
    ap.add_argument("--write", action="store_true", help="Reseal if stale")
    ap.add_argument("--json", action="store_true", help="Machine-readable output")
    args = ap.parse_args(argv)

    root = Path(args.root)
    mpath = Path(args.manifest) if args.manifest else root / "manifests" / "FREE_CORE_SEAL.json"
    fresh = build_free_core_manifest(root)
    fresh_root = fresh.get("merkle_root")
    fresh_count = fresh.get("count")

    if not mpath.exists():
        out = {"ok": False, "reason": "missing_seal", "fresh_merkle_root": fresh_root, "fresh_count": fresh_count}
        if args.write:
            write_manifest(fresh, mpath)
            out = {"ok": True, "wrote": str(mpath), "merkle_root": fresh_root, "count": fresh_count}
            print(json.dumps(out, indent=2) if args.json else f"WROTE {mpath} merkle={fresh_root} count={fresh_count}")
            return 0
        print(json.dumps(out, indent=2) if args.json else f"STALE missing seal; fresh_root={fresh_root}")
        return 1

    existing = load_manifest(mpath)
    existing_root = existing.get("merkle_root")
    ok = existing_root == fresh_root
    result = {
        "ok": ok,
        "existing_merkle_root": existing_root,
        "fresh_merkle_root": fresh_root,
        "existing_count": existing.get("count"),
        "fresh_count": fresh_count,
        "manifest": str(mpath),
    }
    if ok:
        print(json.dumps(result, indent=2) if args.json else f"FRESH merkle={existing_root} count={fresh_count}")
        return 0
    if args.write:
        write_manifest(fresh, mpath)
        result["ok"] = True
        result["wrote"] = True
        print(json.dumps(result, indent=2) if args.json else f"RESEALED {mpath} merkle={fresh_root} count={fresh_count}")
        return 0
    print(json.dumps(result, indent=2) if args.json else (
        f"STALE existing={existing_root} fresh={fresh_root} "
        f"(run: python3 scripts/check_seal_freshness.py --write)"
    ))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
