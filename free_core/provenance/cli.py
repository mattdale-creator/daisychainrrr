"""CLI: ttllm-manifest"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from .manifest import (
    build_merkle_manifest,
    walk_files,
    write_manifest,
    load_manifest,
    verify_manifest,
)
from .hashing import sha256_file


def cmd_hash(args):
    root = Path(args.path)
    files = walk_files(root) if root.is_dir() else [root]
    for f in files:
        print(f"{sha256_file(f)}  {f}")


def cmd_build(args):
    root = Path(args.path)
    files = walk_files(root)
    man = build_merkle_manifest(files, base=root, extra={"source_path": str(root.resolve())})
    out = Path(args.out) if args.out else root / "MANIFEST.ttllm.json"
    write_manifest(man, out)
    print(f"wrote {out}")
    print(f"merkle_root={man['merkle_root']}")
    print(f"count={man['count']}")


def cmd_verify(args):
    man = load_manifest(args.manifest)
    base = Path(args.base) if args.base else Path(".")
    result = verify_manifest(man, base)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["ok"] else 1)


def cmd_seal_repo(args):
    root = Path(args.path)
    # seal free_core, docs, founding (public skeleton)
    targets = []
    for sub in ("free_core", "docs", "founding", "prompts", "registers", "continuity", "site", "examples"):
        p = root / sub
        if p.exists():
            targets.extend(walk_files(p))
    # also top-level key files
    for name in ("README.md", "LICENSE", "pyproject.toml", "Makefile"):
        p = root / name
        if p.is_file():
            targets.append(p)
    man = build_merkle_manifest(targets, base=root, extra={"seal": "free_public_core", "repo": "daisychainrrr"})
    out = root / "manifests" / "FREE_CORE_SEAL.json"
    write_manifest(man, out)
    print(f"sealed {man['count']} files → {out}")
    print(f"merkle_root={man['merkle_root']}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="ttllm-manifest", description="TTLLM cryptographic provenance tools")
    sub = p.add_subparsers(dest="cmd", required=True)

    h = sub.add_parser("hash", help="SHA-256 of file or directory tree")
    h.add_argument("path")
    h.set_defaults(func=cmd_hash)

    b = sub.add_parser("build", help="Build Merkle manifest for a directory")
    b.add_argument("path")
    b.add_argument("-o", "--out", default=None)
    b.set_defaults(func=cmd_build)

    v = sub.add_parser("verify", help="Verify a manifest against a base directory")
    v.add_argument("--manifest", required=True)
    v.add_argument("--base", default=".")
    v.set_defaults(func=cmd_verify)

    s = sub.add_parser("seal-repo", help="Seal free public core of this repository")
    s.add_argument("path", nargs="?", default=".")
    s.set_defaults(func=cmd_seal_repo)

    # also support "seal-repo" via module style
    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
