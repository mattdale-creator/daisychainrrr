#!/usr/bin/env python3
"""First-class inclusion-proof demo for non-CLI humans (fine-grain P0.5).

Writes site/demo/inclusion_proof_sample.json and prints the human recipe.
Does not require network. Free public core — no paywall.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.provenance.manifest import load_manifest  # noqa: E402
from free_core.provenance.proof import inclusion_proof, verify_inclusion  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    path = "README.md"
    if argv and len(argv) > 1:
        path = argv[1]
    mpath = REPO / "manifests" / "FREE_CORE_SEAL.json"
    if not mpath.is_file():
        print("missing FREE_CORE_SEAL", file=sys.stderr)
        return 1
    man = load_manifest(mpath)
    leaves = sorted(man.get("leaves", []), key=lambda x: x["path"])
    paths = [x["path"] for x in leaves]
    if path not in paths:
        print(f"path not in seal: {path}", file=sys.stderr)
        return 1
    idx = paths.index(path)
    digests = [x["sha256"] for x in leaves]
    proof = inclusion_proof(digests, idx)
    proof["path"] = path
    verified = verify_inclusion(proof["leaf_hash"], proof["proof"], man["merkle_root"])
    out = {
        "schema": "ttllm.inclusion_proof_demo.v1",
        "ethos": "product is the proof — offline, unpaid, free public core",
        "manifest": "manifests/FREE_CORE_SEAL.json",
        "path": path,
        "merkle_root": man["merkle_root"],
        "leaf_count": man.get("count"),
        "proof": proof,
        "verified": verified,
        "recipe": [
            "python3 scripts/demo_inclusion_proof.py",
            "python3 -m free_core.provenance.cli proof --manifest manifests/FREE_CORE_SEAL.json --path README.md --check",
            "python3 scripts/public_verify_harness.py",
        ],
        "handbook": "docs/handbook/release/06-inclusion-proof.md",
    }
    dest = REPO / "site" / "demo" / "inclusion_proof_sample.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"verified": verified, "path": path, "wrote": str(dest), "root": man["merkle_root"][:16] + "…"}, indent=2))
    return 0 if verified else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
