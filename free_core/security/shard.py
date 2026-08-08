"""Sharded index integrity binding (founding turn 16)."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Any
from free_core.provenance.hashing import sha256_bytes, sha256_file
from free_core.provenance.manifest import merkle_root


def seal_shards(shard_paths: List[Path], *, base: Path | None = None) -> Dict[str, Any]:
    leaves = []
    for p in sorted(shard_paths):
        p = Path(p)
        rel = str(p.relative_to(base)) if base else str(p)
        leaves.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
    leaves.sort(key=lambda x: x["path"])
    root = merkle_root([x["sha256"] for x in leaves])
    return {
        "schema": "ttllm.shard_manifest.v1",
        "merkle_root": root,
        "count": len(leaves),
        "leaves": leaves,
    }


class ShardManifest:
    def __init__(self, data: dict):
        self.data = data

    @classmethod
    def load(cls, path: Path) -> "ShardManifest":
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    def save(self, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.data, indent=2) + "\n", encoding="utf-8")

    def verify_files(self, base: Path) -> dict:
        missing, bad = [], []
        for leaf in self.data.get("leaves", []):
            p = Path(base) / leaf["path"]
            if not p.is_file():
                missing.append(leaf["path"])
                continue
            if sha256_file(p) != leaf["sha256"]:
                bad.append(leaf["path"])
        ok = not missing and not bad
        return {"ok": ok, "missing": missing, "mismatches": bad}
