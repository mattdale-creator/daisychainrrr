"""
Merkle-style manifests for released artefacts.

Anyone can re-hash released files and confirm they match the published root.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union
from .hashing import sha256_file

PathLike = Union[str, Path]


def merkle_root(leaf_hex_digests: List[str]) -> Optional[str]:
    if not leaf_hex_digests:
        return None
    level = [bytes.fromhex(d) for d in leaf_hex_digests]
    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else left
            next_level.append(hashlib.sha256(left + right).digest())
        level = next_level
    return level[0].hex()


def build_merkle_manifest(
    file_paths: Iterable[PathLike],
    *,
    base: Optional[PathLike] = None,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    base_path = Path(base).resolve() if base else None
    leaves = []
    for p in file_paths:
        path = Path(p)
        if not path.is_file():
            continue
        rel = str(path.resolve().relative_to(base_path)) if base_path else str(path)
        leaves.append({
            "path": rel,
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        })
    leaves.sort(key=lambda x: x["path"])
    root = merkle_root([x["sha256"] for x in leaves])
    manifest: Dict[str, Any] = {
        "schema": "ttllm.manifest.v1",
        "merkle_root": root,
        "count": len(leaves),
        "leaves": leaves,
    }
    if extra:
        manifest["extra"] = extra
    return manifest


def walk_files(root: PathLike, ignore_dirs: Optional[set] = None) -> List[Path]:
    root = Path(root)
    ignore = ignore_dirs or {".git", "__pycache__", ".venv", "node_modules", ".pytest_cache", ".egg-info"}
    out = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in ignore or part.endswith(".egg-info") for part in p.parts):
            continue
        out.append(p)
    return sorted(out)


def verify_manifest(manifest: Dict[str, Any], base: PathLike) -> Dict[str, Any]:
    base = Path(base)
    mismatches = []
    missing = []
    ok = []
    for leaf in manifest.get("leaves", []):
        path = base / leaf["path"]
        if not path.is_file():
            missing.append(leaf["path"])
            continue
        actual = sha256_file(path)
        if actual != leaf["sha256"]:
            mismatches.append({
                "path": leaf["path"],
                "expected": leaf["sha256"],
                "actual": actual,
            })
        else:
            ok.append(leaf["path"])
    expected_root = manifest.get("merkle_root")
    actual_root = merkle_root([
        l["sha256"] for l in sorted(manifest.get("leaves", []), key=lambda x: x["path"])
    ])
    return {
        "ok": not mismatches and not missing and expected_root == actual_root,
        "merkle_root_matches_leaves": expected_root == actual_root,
        "merkle_root_expected": expected_root,
        "merkle_root_from_leaves": actual_root,
        "verified_files": len(ok),
        "mismatches": mismatches,
        "missing": missing,
    }


def write_manifest(manifest: Dict[str, Any], path: PathLike) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2, sort_keys=False) + chr(10), encoding="utf-8")
    return path


def load_manifest(path: PathLike) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))
