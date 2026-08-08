#!/usr/bin/env python3
"""One-shot unpaid public proof — product is the proof.

Runs the free-core checks anyone can run from a cold checkout with no auth
and no payment, then writes site/demo/public_proof.json for the status page.

Founding load path: free public core never paywalled; soft tissue is claiming
green without re-measurement.
"""
from __future__ import annotations
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core import __version__  # noqa: E402
from free_core.provenance.manifest import load_manifest, verify_manifest  # noqa: E402
from free_core.provenance.proof import inclusion_proof, verify_inclusion  # noqa: E402
from free_core.provenance.seal_targets import build_free_core_manifest  # noqa: E402
from free_core.stream.log import StreamLog  # noqa: E402
from free_core.stream.nano_tips import collect_nano_stream_tips  # noqa: E402
from free_core.status import collect_status  # noqa: E402


def _run_harness() -> dict:
    p = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "public_verify_harness.py")],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    fails: list = []
    ok = p.returncode == 0
    # parse last JSON line if present
    for line in reversed((p.stdout or "").splitlines()):
        line = line.strip()
        if line.startswith("{") and "fails" in line:
            try:
                j = json.loads(line)
                fails = j.get("fails") or []
                ok = bool(j.get("ok"))
            except json.JSONDecodeError:
                pass
            break
    return {"ok": ok, "exit_code": p.returncode, "fails": fails, "command": "python3 scripts/public_verify_harness.py"}


def build_proof() -> dict:
    mpath = REPO / "manifests" / "FREE_CORE_SEAL.json"
    seal: dict = {"present": mpath.is_file()}
    if mpath.is_file():
        man = load_manifest(mpath)
        ver = verify_manifest(man, REPO)
        fresh = build_free_core_manifest(REPO)
        seal.update(
            {
                "verify_ok": bool(ver.get("ok")),
                "fresh": man.get("merkle_root") == fresh.get("merkle_root"),
                "merkle_root": man.get("merkle_root"),
                "count": man.get("count"),
                "green": bool(ver.get("ok")) and man.get("merkle_root") == fresh.get("merkle_root"),
            }
        )
        # inclusion for README
        leaves = sorted(man.get("leaves", []), key=lambda x: x["path"])
        paths = [x["path"] for x in leaves]
        if "README.md" in paths:
            idx = paths.index("README.md")
            digests = [x["sha256"] for x in leaves]
            proof = inclusion_proof(digests, idx)
            seal["inclusion_readme_ok"] = verify_inclusion(
                proof["leaf_hash"], proof["proof"], man["merkle_root"]
            )
        else:
            seal["inclusion_readme_ok"] = False

    tips = collect_nano_stream_tips(REPO)
    st = collect_status(REPO)
    harness = _run_harness()

    checks = {
        "free_core_seal_green": bool(seal.get("green")),
        "inclusion_readme": bool(seal.get("inclusion_readme_ok")),
        "public_verify_harness": bool(harness.get("ok")),
        "nano_streams_all_chain_ok": bool(tips.get("all_chain_ok")),
        "boundary_named": (REPO / "commercial" / "BOUNDARY.md").is_file(),
        "founding_transcript_present": (
            REPO / "founding" / "conversation" / "TRANSCRIPT_ONLY.md"
        ).is_file(),
    }
    all_ok = all(checks.values())

    return {
        "schema": "ttllm.public_proof.v1",
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "free_core_version": __version__,
        "ethos": {
            "product_is_the_proof": True,
            "free_public_core_never_paywalled": True,
            "green_means_verify_and_fresh": True,
            "nano_is_not_frontier": True,
            "hard_gates_not_faked": True,
        },
        "direction": {
            "on_track": True,
            "why": (
                "Building free-core proof surface + nano shape + org bone from founding SoT; "
                "not faking T1–T11 or claiming OLMo-scale."
            ),
            "not_doing": [
                "paywalled verification",
                "silent hard-gate close",
                "frontier capability cosplay",
                "Matrix aesthetic without real stream/ttlink data",
            ],
            "founding_load_path": "founding/conversation/USER_PROMPTS.md + TRANSCRIPT_ONLY.md",
        },
        "checks": checks,
        "all_ok": all_ok,
        "seal": seal,
        "nano_streams": {
            "all_chain_ok": tips.get("all_chain_ok"),
            "nano_count": tips.get("nano_count"),
            "tips": [
                {"name": n.get("name"), "chain_ok": n.get("chain_ok"), "tip": n.get("tip"), "count": n.get("count")}
                for n in tips.get("nanos", [])
            ],
        },
        "harness": harness,
        "status_seal": (st.get("seal") or {}),
        "recipe": [
            "git clone https://github.com/mattdale-creator/daisychainrrr",
            "cd daisychainrrr",
            "python3 scripts/public_proof.py",
            "python3 scripts/public_verify_harness.py",
            "python3 scripts/oneshot_verify_all.py",
            "python3 scripts/ttllm_status.py --quiet-ok",
        ],
        "contact": "md@0265.au",
        "site": "https://ttllms.com",
    }


def main() -> int:
    proof = build_proof()
    out = REPO / "site" / "demo" / "public_proof.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(proof, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "all_ok": proof["all_ok"],
                "free_core_version": proof["free_core_version"],
                "checks": proof["checks"],
                "wrote": str(out.relative_to(REPO)),
                "direction_on_track": proof["direction"]["on_track"],
            },
            indent=2,
        )
    )
    return 0 if proof["all_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
