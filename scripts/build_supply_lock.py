#!/usr/bin/env python3
"""Build supply-chain lock artefact for free_core (Domain 7).

Hashes pyproject.toml + optional requirements files + free_core package tree tip.
Writes registers/supply-chain/SUPPLY_LOCK.json and .sha256 text.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.provenance.hashing import sha256_file  # noqa: E402
from free_core.provenance.manifest import build_merkle_manifest, walk_files, write_manifest  # noqa: E402


def main() -> int:
    out_dir = REPO / "registers" / "supply-chain"
    out_dir.mkdir(parents=True, exist_ok=True)

    files = []
    for name in ("pyproject.toml", "Makefile", "LICENSE"):
        p = REPO / name
        if p.is_file():
            files.append(p)
    # declared deps are empty runtime; still seal free_core tree
    fc = REPO / "free_core"
    if fc.is_dir():
        files.extend(walk_files(fc))

    man = build_merkle_manifest(
        files,
        base=REPO,
        extra={
            "schema": "ttllm.supply_lock.v1",
            "note": "runtime deps empty; optional cryptography/pytest via extras",
        },
    )
    lock_path = out_dir / "SUPPLY_LOCK.json"
    write_manifest(man, lock_path)
    # also a simple sha256 of pyproject
    py_sha = sha256_file(REPO / "pyproject.toml") if (REPO / "pyproject.toml").is_file() else None
    meta = {
        "schema": "ttllm.supply_meta.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "pyproject_sha256": py_sha,
        "merkle_root": man["merkle_root"],
        "count": man["count"],
        "lock_path": "registers/supply-chain/SUPPLY_LOCK.json",
        "optional_extras": ["dev:pytest", "crypto:cryptography"],
    }
    meta_path = out_dir / "SUPPLY_META.json"
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (out_dir / "SUPPLY_LOCK.sha256").write_text(
        f"{man['merkle_root']}  SUPPLY_LOCK.json\n{py_sha}  pyproject.toml\n",
        encoding="utf-8",
    )
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
