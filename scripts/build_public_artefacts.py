#!/usr/bin/env python3
"""Build demo index, stream log, seal, optional demo signature."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from free_core.ttlink.index import TtlinkIndex
from free_core.stream.schema import demo_events, StreamEvent
from free_core.stream.log import StreamLog
from free_core.provenance.cli import cmd_seal_repo
from free_core.provenance.hashing import sha256_file


class Args:
    path = str(ROOT)


def main():
    # ttlink index from corpus
    idx = TtlinkIndex()
    n = idx.index_directory(ROOT / "examples" / "corpus")
    idx.save(ROOT / "examples" / "ttlink_index.json")
    # also copy to site for browser demo
    site_demo = ROOT / "site" / "demo" / "ttlink_index.json"
    idx.save(site_demo)
    binding = idx.manifest_binding()
    (ROOT / "examples" / "ttlink_binding.json").write_text(
        json.dumps(binding, indent=2) + "\n", encoding="utf-8"
    )
    print(f"ttlink: {n} docs → examples/ + site/demo/")

    # stream log
    log = StreamLog()
    for e in demo_events():
        log.append(e)
    # add build event
    log.append(StreamEvent(
        event_type="build",
        payload={"script": "scripts/build_public_artefacts.py", "ttlink_docs": n},
    ))
    log_path = ROOT / "examples" / "stream" / "public_log.json"
    log.save(log_path)
    (ROOT / "site" / "demo" / "public_log.json").write_text(log_path.read_text(), encoding="utf-8")
    print("stream:", log.verify_chain())

    # seal repo
    from argparse import Namespace
    from free_core.provenance import cli as mcli
    mcli.cmd_seal_repo(Namespace(path=str(ROOT)))

    # demo key + signed seal (demo keys are public examples; not production trust)
    try:
        from free_core.provenance.sign import write_keypair, sign_manifest
        from free_core.provenance.manifest import load_manifest
        keys = ROOT / "examples" / "keys"
        # regenerate only if missing public (private also demo-only, gitignored ideally)
        priv_p = keys / "demo.private.pem"
        pub_p = keys / "demo.public.pem"
        if not pub_p.exists() or not priv_p.exists():
            write_keypair(keys, name="demo")
        man = load_manifest(ROOT / "manifests" / "FREE_CORE_SEAL.json")
        signed = sign_manifest(man, priv_p.read_bytes())
        out = ROOT / "manifests" / "FREE_CORE_SEAL.signed.json"
        out.write_text(json.dumps(signed, indent=2) + "\n", encoding="utf-8")
        # publish public key only to site
        (ROOT / "site" / "demo" / "demo.public.pem").write_bytes(pub_p.read_bytes())
        (ROOT / "examples" / "keys" / "README.md").write_text(
            "# Demo keys\n\n`demo.private.pem` is for **local demo only** — not a production root of trust.\n"
            "Publish `demo.public.pem` with signed manifests for tutorial verification.\n"
            "Rotate to HSM/org keys before any production release.\n",
            encoding="utf-8",
        )
        print("signed seal →", out)
    except Exception as e:
        print("sign skipped:", e)

    print("done")


if __name__ == "__main__":
    main()
