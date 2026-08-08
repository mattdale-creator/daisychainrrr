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
    "version": "0.6.4",
}


# Volatile probe outputs — must not invalidate FREE_CORE_SEAL after every harness run
SEAL_EXCLUDE_NAMES = {
    "last_harness_run.json",
    "last_dns_status.json",
    "last_check.json",
    "last_registration_ttllms_com.json",
    "last_registration_ttllms_org.json",
    "last_status_ttllms_com.json",
    "last_status_ttllms_org.json",
    "secrets.local.env",
    # Generated snapshot for site demo; refreshed without resealing free core
    "status_snapshot.json",
    # Regenerated from current FREE_CORE_SEAL; would self-stale if sealed
    "inclusion_proof_sample.json",
    # Testing-loop automated run summary (volatile)
    "last_testing_loop_run.json",
    # Last unpaid public-proof run (wall-clock; must not thrash seal)
    "public_proof.json",
    # Commercial status snapshot (pre-revenue; regenerated)
    "commercial_status.json",
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
    filtered: List[Path] = []
    for t in targets:
        if t.name in SEAL_EXCLUDE_NAMES:
            continue
        if t.suffix == ".pyc" or "__pycache__" in t.parts:
            continue
        # Volatile red-team run outputs (re-run should not invalidate FREE_CORE_SEAL)
        if t.name.startswith("campaign_") and t.suffix == ".json":
            continue
        if t.name == "last_harness_run.json":
            continue
        # Never seal private key material (even tutorial keys) into free-core Merkle seal
        name_l = t.name.lower()
        if name_l.endswith(".private.pem") or name_l.endswith(".priv") or name_l == "private.pem":
            continue
        if name_l.endswith(".key") and "public" not in name_l:
            continue
        filtered.append(t)
    return filtered


def build_free_core_manifest(root: Path) -> dict:
    root = Path(root)
    targets = collect_seal_targets(root)
    return build_merkle_manifest(targets, base=root, extra=dict(SEAL_EXTRA))
