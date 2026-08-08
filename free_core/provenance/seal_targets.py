"""Canonical free-public-core seal target set (shared by CLI + freshness check)."""
from __future__ import annotations
from pathlib import Path
from typing import List

from .manifest import walk_files, build_merkle_manifest

# Directories sealed into FREE_CORE_SEAL
SEAL_SUBDIRS = (
    "free_core",
    "docs",
    "founding",
    "prompts",
    "registers",
    "continuity",
    "site",
    "examples",
    "commercial",
    "scripts",
)

SEAL_ROOT_FILES = (
    "README.md",
    "LICENSE",
    "pyproject.toml",
    "Makefile",
)

SEAL_EXTRA = {
    "seal": "free_public_core",
    "repo": "daisychainrrr",
    "version": "0.5.0",
}


def collect_seal_targets(root: Path) -> List[Path]:
    root = Path(root)
    targets: List[Path] = []
    for sub in SEAL_SUBDIRS:
        p = root / sub
        if p.exists():
            targets.extend(walk_files(p))
    for name in SEAL_ROOT_FILES:
        p = root / name
        if p.is_file():
            targets.append(p)
    return targets


def build_free_core_manifest(root: Path) -> dict:
    root = Path(root)
    targets = collect_seal_targets(root)
    return build_merkle_manifest(targets, base=root, extra=dict(SEAL_EXTRA))
