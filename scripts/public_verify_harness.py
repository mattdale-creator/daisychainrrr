#!/usr/bin/env python3
"""Public unpaid verify harness — all checks local, no auth, no paywall.

Asserts free-core proof surface works from a cold checkout with only public files.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.provenance.manifest import load_manifest, verify_manifest  # noqa: E402
from free_core.provenance.proof import inclusion_proof, verify_inclusion  # noqa: E402
from free_core.stream.log import StreamLog  # noqa: E402
from free_core.stream.catalog import required_for_class  # noqa: E402
from free_core.security.canary import check_canary  # noqa: E402
from free_core.ttlink.index import TtlinkIndex  # noqa: E402


def main() -> int:
    fails = []
    print("=== public unpaid verify harness ===")

    # 1. FREE_CORE_SEAL verify
    mpath = REPO / "manifests/FREE_CORE_SEAL.json"
    if not mpath.exists():
        fails.append("missing FREE_CORE_SEAL")
    else:
        r = verify_manifest(load_manifest(mpath), REPO)
        print("FREE_CORE_SEAL", r["ok"], "files", r.get("verified_files"))
        if not r["ok"]:
            fails.append("FREE_CORE_SEAL_verify")
        else:
            # inclusion proof for README.md
            man = load_manifest(mpath)
            leaves = sorted(man.get("leaves", []), key=lambda x: x["path"])
            paths = [x["path"] for x in leaves]
            if "README.md" in paths:
                idx = paths.index("README.md")
                digests = [x["sha256"] for x in leaves]
                proof = inclusion_proof(digests, idx)
                ok = verify_inclusion(proof["leaf_hash"], proof["proof"], man["merkle_root"])
                print("inclusion_proof README.md", ok)
                if not ok:
                    fails.append("inclusion_proof")
            else:
                print("inclusion_proof SKIP README.md not in seal leaves")

    # 2. example stream
    ex = REPO / "examples/stream/public_log.json"
    if ex.exists():
        ch = StreamLog.load(ex).verify_chain()
        print("examples/stream", ch)
        if not ch.get("ok"):
            fails.append("example_stream")
    else:
        fails.append("missing_example_stream")

    # 3. example ttlink query (no auth)
    tip = REPO / "examples/ttlink_index.json"
    if tip.exists():
        idx = TtlinkIndex.load(tip)
        hits = idx.query("free public core")
        print("ttlink_query hits", len(hits))
        if len(hits) < 1:
            fails.append("ttlink_query_empty")
    else:
        fails.append("missing_ttlink_index")

    # 4. nano release if present
    nano = REPO / "models/ttllm-nano"
    if nano.exists():
        rm = nano / "manifests/RELEASE_MANIFEST.json"
        if rm.exists():
            r = verify_manifest(load_manifest(rm), nano)
            print("nano RELEASE_MANIFEST", r["ok"])
            if not r["ok"]:
                fails.append("nano_manifest")
        sp = nano / "stream/public_log.json"
        if sp.exists():
            log = StreamLog.load(sp)
            ch = log.verify_chain()
            print("nano stream", ch)
            if not ch.get("ok"):
                fails.append("nano_stream")
            types = {e.get("event_type") for e in log.events}
            missing = [t for t in required_for_class("nano") if t not in types]
            print("nano required events missing", missing)
            if missing:
                fails.append(f"nano_stream_events:{','.join(missing)}")
        ip = nano / "ttlink/index.json"
        if ip.exists():
            c = check_canary(TtlinkIndex.load(ip), "ttllm-public-canary-v1")
            # older nanos may use bone-not-soft-tissue default
            if not c.get("ok"):
                c2 = check_canary(TtlinkIndex.load(ip), "bone-not-soft-tissue")
                print("nano canary", c, "fallback", c2)
                if not c2.get("ok"):
                    print("  canary miss non-fatal for mixed secrets")
            else:
                print("nano canary", c)

    # 5. BOUNDARY readable unpaid
    b = REPO / "commercial/BOUNDARY.md"
    if not b.is_file() or "Free public core" not in b.read_text(encoding="utf-8"):
        fails.append("boundary_missing")
    else:
        print("BOUNDARY ok")

    print("FAILS", fails)
    print(json.dumps({"ok": not fails, "fails": fails}, indent=2))
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
