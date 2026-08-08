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
from .proof import inclusion_proof, verify_inclusion


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
    from .seal_targets import build_free_core_manifest
    root = Path(args.path)
    man = build_free_core_manifest(root)
    out = root / "manifests" / "FREE_CORE_SEAL.json"
    write_manifest(man, out)
    print(f"sealed {man['count']} files → {out}")
    print(f"merkle_root={man['merkle_root']}")


def cmd_proof(args):
    man = load_manifest(args.manifest)
    leaves = sorted(man.get("leaves", []), key=lambda x: x["path"])
    digests = [x["sha256"] for x in leaves]
    if args.path:
        paths = [x["path"] for x in leaves]
        try:
            idx = paths.index(args.path)
        except ValueError:
            print(f"path not in manifest: {args.path}", file=sys.stderr)
            sys.exit(1)
    else:
        idx = args.index
    proof = inclusion_proof(digests, idx)
    proof["path"] = leaves[idx]["path"]
    print(json.dumps(proof, indent=2))
    if args.check:
        ok = verify_inclusion(proof["leaf_hash"], proof["proof"], man["merkle_root"])
        print(json.dumps({"verified": ok, "expected_root": man["merkle_root"]}))
        sys.exit(0 if ok else 1)


def cmd_keygen(args):
    from .sign import write_keypair
    priv, pub = write_keypair(args.out, name=args.name)
    print(f"wrote {priv}")
    print(f"wrote {pub}")
    print("KEEP private key secret. Publish only the public key.")


def cmd_sign(args):
    from .sign import sign_manifest
    man = load_manifest(args.manifest)
    priv = Path(args.key).read_bytes()
    signed = sign_manifest(man, priv)
    out = Path(args.out) if args.out else Path(str(args.manifest) + ".signed.json")
    out.write_text(json.dumps(signed, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out}")


def cmd_verify_sig(args):
    from .sign import verify_signed_manifest
    signed = json.loads(Path(args.signed).read_text(encoding="utf-8"))
    pub = Path(args.pubkey).read_bytes()
    ok = verify_signed_manifest(signed, pub)
    # also verify leaf hashes consistency
    man = signed["manifest"]
    base = Path(args.base) if args.base else None
    result = {"signature_ok": ok}
    if base:
        result["files"] = verify_manifest(man, base)
    print(json.dumps(result, indent=2))
    sys.exit(0 if ok and (base is None or result["files"]["ok"]) else (0 if ok and base is None else 1))


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

    pr = sub.add_parser("proof", help="Merkle inclusion proof for a leaf")
    pr.add_argument("--manifest", required=True)
    pr.add_argument("--index", type=int, default=0)
    pr.add_argument("--path", default=None, help="leaf path instead of index")
    pr.add_argument("--check", action="store_true")
    pr.set_defaults(func=cmd_proof)

    kg = sub.add_parser("keygen", help="Generate Ed25519 keypair (requires cryptography)")
    kg.add_argument("-o", "--out", default="keys")
    kg.add_argument("--name", default="ttllm")
    kg.set_defaults(func=cmd_keygen)

    sg = sub.add_parser("sign", help="Sign a manifest with Ed25519 private key")
    sg.add_argument("--manifest", required=True)
    sg.add_argument("--key", required=True)
    sg.add_argument("-o", "--out", default=None)
    sg.set_defaults(func=cmd_sign)

    vs = sub.add_parser("verify-sig", help="Verify signed manifest")
    vs.add_argument("--signed", required=True)
    vs.add_argument("--pubkey", required=True)
    vs.add_argument("--base", default=None)
    vs.set_defaults(func=cmd_verify_sig)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
