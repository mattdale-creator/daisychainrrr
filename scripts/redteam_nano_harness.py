#!/usr/bin/env python3
"""Adversarial harness against transparency layer (founding turns 14–16)."""
from __future__ import annotations
import json, sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from free_core.provenance.manifest import build_merkle_manifest, verify_manifest
from free_core.stream.log import StreamLog
from free_core.stream.schema import StreamEvent
from free_core.security.query_guard import QueryGuard
from free_core.security.canary import inject_canary, check_canary
from free_core.ttlink.index import TtlinkIndex

def main():
    results = []
    ex = list((REPO / "examples" / "corpus").glob("*.txt"))
    if ex:
        man = build_merkle_manifest(ex, base=REPO)
        ok1 = verify_manifest(man, REPO)["ok"]
        man2 = json.loads(json.dumps(man))
        man2["leaves"][0]["sha256"] = "0" * 64
        ok2 = verify_manifest(man2, REPO)["ok"]
        results.append({"test": "manifest_tamper_detected", "pass": ok1 and (ok2 is False)})
    log = StreamLog()
    log.append(StreamEvent(event_type="a", payload={"n": 1}))
    log.append(StreamEvent(event_type="b", payload={"n": 2}))
    ok_chain = log.verify_chain()["ok"]
    log.events[1]["payload"]["n"] = 99
    broken = log.verify_chain()["ok"] is False
    results.append({"test": "stream_tamper_detected", "pass": ok_chain and broken})
    g = QueryGuard(hard_limit=3)
    allowed = sum(1 for _ in range(3) if g.allow("x"))
    blocked = g.allow("x") is False
    results.append({"test": "query_guard_rate_limit", "pass": allowed == 3 and blocked})
    idx = TtlinkIndex()
    inject_canary(idx, "harness")
    results.append({"test": "canary_present", "pass": check_canary(idx, "harness")["ok"]})
    idx2 = TtlinkIndex()
    results.append({"test": "canary_absent", "pass": check_canary(idx2, "harness")["ok"] is False})
    # BOUNDARY must exist and forbid paywalling verification language
    bpath = REPO / "commercial" / "BOUNDARY.md"
    btxt = bpath.read_text(encoding="utf-8") if bpath.is_file() else ""
    results.append({
        "test": "boundary_forbids_paywall_verify",
        "pass": "Paywall on verifying" in btxt or "Paywall on verifying a public-core claim" in btxt
        or ("paywall" in btxt.lower() and "verif" in btxt.lower()),
    })
    # Free core seal present + verifies (integrity of public claim surface)
    from free_core.provenance.manifest import load_manifest
    mpath = REPO / "manifests" / "FREE_CORE_SEAL.json"
    if mpath.is_file():
        results.append({
            "test": "free_core_seal_verifies",
            "pass": bool(verify_manifest(load_manifest(mpath), REPO).get("ok")),
        })
    else:
        results.append({"test": "free_core_seal_verifies", "pass": False})
    # Inclusion proof path exists (tooling)
    from free_core.provenance.proof import inclusion_proof, verify_inclusion
    if mpath.is_file():
        man = load_manifest(mpath)
        leaves = sorted(man.get("leaves") or [], key=lambda x: x["path"])
        digests = [x["sha256"] for x in leaves]
        if digests:
            pr = inclusion_proof(digests, 0)
            results.append({
                "test": "inclusion_proof_roundtrip",
                "pass": verify_inclusion(pr["leaf_hash"], pr["proof"], man["merkle_root"]),
            })
    # Founding discipline doc present
    drugs = REPO / "docs" / "security" / "REMEMBER_YOU_ARE_ON_DRUGS.md"
    results.append({
        "test": "remember_on_drugs_checklist_present",
        "pass": drugs.is_file() and "public_verify_harness" in drugs.read_text(encoding="utf-8"),
    })
    # Claim gate present
    cg = REPO / "docs" / "specs" / "artefacts" / "04" / "PUBLIC_CLAIM_GATE.md"
    results.append({
        "test": "public_claim_gate_present",
        "pass": cg.is_file() and "frontier" in cg.read_text(encoding="utf-8").lower(),
    })
    out = {"schema": "ttllm.redteam_harness.v1", "results": results, "all_pass": all(r["pass"] for r in results)}
    path = REPO / "registers" / "redteam" / "last_harness_run.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    sys.exit(0 if out["all_pass"] else 1)

if __name__ == "__main__":
    main()
