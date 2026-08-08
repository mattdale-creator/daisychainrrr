#!/usr/bin/env python3
"""One-shot verification of free core + all nano releases + fine-grain gates."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from free_core.provenance.manifest import load_manifest, verify_manifest
from free_core.stream.log import StreamLog
from free_core.security.canary import check_canary
from free_core.ttlink.index import TtlinkIndex


def _run(script: str, *args: str) -> int:
    cmd = [sys.executable, str(REPO / "scripts" / script), *args]
    print("RUN", " ".join(cmd))
    return subprocess.call(cmd, cwd=str(REPO))


def main():
    fails = []
    # free core seal
    mpath = REPO / "manifests/FREE_CORE_SEAL.json"
    if mpath.exists():
        r = verify_manifest(load_manifest(mpath), REPO)
        print("FREE_CORE_SEAL", r["ok"], "files", r.get("verified_files"))
        if not r["ok"]:
            fails.append("FREE_CORE_SEAL")
    else:
        fails.append("FREE_CORE_SEAL_missing")

    for name in ["ttllm-nano", "ttllm-nano-v2", "ttllm-nano-v3", "ttllm-nano-v4"]:
        root = REPO / "models" / name
        if not root.exists():
            continue
        ck = root / "manifests/CHECKPOINTS_MANIFEST.json"
        if ck.exists():
            r = verify_manifest(load_manifest(ck), REPO)
            print(name, "ckpts", r["ok"], r.get("verified_files"), "missing", len(r.get("missing") or []))
            if not r["ok"]:
                fails.append(f"{name}-ckpts")
        sp = root / "stream/public_log.json"
        if sp.exists():
            ch = StreamLog.load(sp).verify_chain()
            print(name, "stream", ch)
            if not ch.get("ok"):
                fails.append(f"{name}-stream")
        ip = root / "ttlink/index.json"
        if ip.exists():
            idx = TtlinkIndex.load(ip)
            c = check_canary(idx, "ttllm-public-canary-v1")
            print(name, "canary", c.get("ok"))
            if not c.get("ok"):
                c2 = check_canary(idx, "bone-not-soft-tissue")
                print("  fallback canary", c2.get("ok"), "(non-fatal if legacy index)")

    # Fine-grain automated bone
    if _run("check_seal_freshness.py") != 0:
        fails.append("seal_freshness")
    if _run("check_data_cards.py") != 0:
        fails.append("data_cards")
    if _run("public_verify_harness.py") != 0:
        fails.append("public_verify_harness")

    print("FAILS", fails)
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())

