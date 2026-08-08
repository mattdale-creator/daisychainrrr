"""Machine-readable project status for free public core (no secrets)."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from free_core import __version__
from free_core.provenance.manifest import load_manifest, verify_manifest
from free_core.provenance.seal_targets import build_free_core_manifest


def _repo_root(start: Path | None = None) -> Path:
    if start is None:
        start = Path.cwd()
    start = Path(start).resolve()
    for p in [start, *start.parents]:
        if (p / "manifests" / "FREE_CORE_SEAL.json").exists() or (p / "free_core").is_dir():
            return p
    return start


def collect_status(repo: Path | None = None) -> Dict[str, Any]:
    root = _repo_root(repo)
    mpath = root / "manifests" / "FREE_CORE_SEAL.json"
    seal: Dict[str, Any] = {"present": mpath.is_file()}
    if mpath.is_file():
        man = load_manifest(mpath)
        ver = verify_manifest(man, root)
        fresh = build_free_core_manifest(root)
        seal.update({
            "merkle_root": man.get("merkle_root"),
            "count": man.get("count"),
            "verify_ok": bool(ver.get("ok")),
            "fresh": man.get("merkle_root") == fresh.get("merkle_root"),
            "fresh_merkle_root": fresh.get("merkle_root"),
            "fresh_count": fresh.get("count"),
        })
    nanos: List[Dict[str, Any]] = []
    models = root / "models"
    if models.is_dir():
        for d in sorted(models.glob("ttllm-nano*")):
            if not d.is_dir():
                continue
            rm = d / "manifests" / "RELEASE_MANIFEST.json"
            entry: Dict[str, Any] = {"name": d.name, "release_manifest": rm.is_file()}
            if rm.is_file():
                r = verify_manifest(load_manifest(rm), d)
                entry["verify_ok"] = bool(r.get("ok"))
                entry["merkle_root"] = load_manifest(rm).get("merkle_root")
                if not r.get("ok"):
                    entry["mismatches"] = (r.get("mismatches") or [])[:5]
            nanos.append(entry)
    hard = root / "docs" / "HARD_TECHNOLOGICAL_GATES.md"
    return {
        "schema": "ttllm.project_status.v1",
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "free_core_version": __version__,
        "repo": str(root),
        "seal": seal,
        "nanos": nanos,
        "hard_gates_doc": hard.is_file(),
        "ethos": {
            "free_public_core_never_paywalled": True,
            "nano_is_not_frontier": True,
            "hard_gates_not_faked": True,
        },
        "commands": {
            "verify": "python3 scripts/public_verify_harness.py",
            "seal_freshness": "python3 scripts/check_seal_freshness.py",
            "redteam": "python3 scripts/redteam_nano_harness.py",
        },
    }


def status_json(repo: Path | None = None) -> str:
    return json.dumps(collect_status(repo), indent=2) + "\n"


def main(argv: list[str] | None = None) -> int:
    """CLI entry for `ttllm-status`."""
    import argparse
    import sys

    ap = argparse.ArgumentParser(prog="ttllm-status", description="TTLLM free-core project status")
    ap.add_argument("--write-site", action="store_true", help="Write site/demo/status_snapshot.json")
    ap.add_argument("--quiet-ok", action="store_true", help="Exit 1 if seal not verify+fresh")
    ap.add_argument("--repo", default=None, help="Repo root (default: walk from cwd / package)")
    args = ap.parse_args(argv)
    if args.repo:
        root = Path(args.repo).resolve()
    else:
        pkg_root = Path(__file__).resolve().parents[1]
        root = pkg_root if (pkg_root / "free_core").is_dir() else Path.cwd()
        root = _repo_root(root)
    st = collect_status(root)
    print(json.dumps(st, indent=2))
    if args.write_site:
        out = root / "site" / "demo" / "status_snapshot.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        pub = dict(st)
        pub["repo"] = "daisychainrrr (public)"
        out.write_text(json.dumps(pub, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out}", file=sys.stderr)
    if args.quiet_ok:
        seal = st.get("seal") or {}
        if not (seal.get("verify_ok") and seal.get("fresh")):
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
