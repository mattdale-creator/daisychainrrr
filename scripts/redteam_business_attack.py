#!/usr/bin/env python3
"""
Black-hat business attack simulation — constructive Domain 8 / 10 QA.

Hostile personas (code-enforced probes, not crime):
  A. Investor capture — force close-core terms
  B. Open-washing competitor — claim TTLLM without bone
  C. Free-rider — take free core, starve commercial
  D. Customer coercion — exclusive weights / paywalled verify
  E. Reputation FUD — false complete / sold claims
  F. Single-human kill — concentration without succession bone
  G. Verify-paywall — break unpaid verify path

Uses real free_core.business.boundary_guard + network/CLI checks.
"""
from __future__ import annotations
import json
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.business.boundary_guard import scan_repo_for_close_core_claims  # noqa: E402
from free_core.provenance.manifest import load_manifest, verify_manifest  # noqa: E402


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def probe(findings: list, fid: str, sev: str, persona: str, title: str, ok: bool, detail: str, residual: str = ""):
    findings.append({
        "id": fid,
        "severity": sev,
        "persona": persona,
        "title": title,
        "pass": ok,
        "detail": detail,
        "residual": residual,
    })


def http_get(url: str, timeout: float = 15.0) -> tuple[int | None, str, str]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ttllm-business-redteam/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(100_000).decode("utf-8", errors="replace")
            return resp.status, resp.headers.get("Content-Type", ""), body
    except urllib.error.HTTPError as e:
        try:
            body = e.read(50_000).decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return e.code, "", body
    except Exception as e:
        return None, "", str(e)


def main() -> int:
    findings: list[dict] = []

    # --- A/B/D/E: static capture-language + SKU + site ---
    scan = scan_repo_for_close_core_claims(REPO)
    high = [f for f in scan.findings if f.severity in ("Critical", "High")]
    probe(
        findings,
        "BH-001",
        "Critical",
        "investor_capture+customer_coercion+openwash",
        "No High/Critical close-core claims in commercial/site/business surfaces",
        len(high) == 0,
        json.dumps([f.to_dict() for f in high[:20]], indent=2) if high else f"scanned ok stats={scan.stats}",
    )

    # --- G: unpaid verify path (local, real code) ---
    mpath = REPO / "manifests" / "FREE_CORE_SEAL.json"
    local_verify = False
    if mpath.is_file():
        local_verify = bool(verify_manifest(load_manifest(mpath), REPO).get("ok"))
    probe(
        findings,
        "BH-002",
        "Critical",
        "verify_paywall",
        "FREE_CORE_SEAL verifies offline without auth/payment",
        local_verify,
        f"path={mpath} ok={local_verify}",
    )

    # public_verify_harness subprocess
    r = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "public_verify_harness.py")],
        cwd=str(REPO),
        capture_output=True,
        text=True,
    )
    probe(
        findings,
        "BH-003",
        "Critical",
        "verify_paywall",
        "public_verify_harness exits 0 (unpaid proof path)",
        r.returncode == 0,
        (r.stdout or "")[-500:],
    )

    # --- G: live site verify docs not behind login ---
    for url_id, url in [
        ("status", "https://ttllms.com/status"),
        ("free_core", "https://ttllms.com/free-core"),
        ("hard_gates", "https://ttllms.com/hard-gates"),
    ]:
        code, ctype, body = http_get(url)
        ok = code == 200 and "login" not in body.lower()[:2000] and "sign in" not in body.lower()[:2000]
        # free-core page should mention verify
        if url_id == "free_core":
            ok = ok and ("verify" in body.lower() or "public" in body.lower())
        probe(
            findings,
            f"BH-004-{url_id}",
            "High",
            "verify_paywall",
            f"Public page {url} returns 200 without login wall",
            ok,
            f"status={code} ctype={ctype[:40]}",
        )

    # --- C: free-rider — free core artefacts exist and are open ---
    bone = [
        REPO / "commercial" / "BOUNDARY.md",
        REPO / "free_core" / "__init__.py",
        REPO / "manifests" / "FREE_CORE_SEAL.json",
        REPO / "models" / "ttllm-nano" / "code" / "train.py",
    ]
    missing = [str(p.relative_to(REPO)) for p in bone if not p.exists()]
    probe(
        findings,
        "BH-005",
        "High",
        "free_rider",
        "Free-core bone paths exist (attacker can clone without paying)",
        len(missing) == 0,
        f"missing={missing}",
        residual="Free-rider is by design; commercial outer must still be valuable",
    )

    # --- F: single-human concentration documented (not hidden) ---
    inv = (REPO / "continuity" / "ASSET_INVENTORY.md").read_text(encoding="utf-8", errors="replace")
    concentration = "unnamed" in inv.lower() or "single-human" in inv.lower() or "tombstone" in inv.lower()
    probe(
        findings,
        "BH-006",
        "High",
        "single_human_kill",
        "Single-human concentration is public (not soft-tissue hidden)",
        concentration,
        "ASSET_INVENTORY must admit backup gaps",
        residual="T9 second custodian still open — attack surface remains until human appoint",
    )

    # --- A: term sheet refuse language present in placeholder ---
    ts = REPO / "docs/placeholders/capital/TERM_SHEET_EXAMPLE.md"
    ts_ok = False
    if ts.is_file():
        t = ts.read_text(encoding="utf-8")
        ts_ok = "Free Public Core" in t and ("No Close-Core" in t or "close-core" in t.lower() or "side letter" in t.lower())
    probe(
        findings,
        "BH-007",
        "Medium",
        "investor_capture",
        "Term sheet example contains free-core covenants / side-letter refuse",
        ts_ok,
        str(ts),
    )

    # --- B: refuse handbook exists ---
    refuse = REPO / "docs/handbook/commercial/02-refuse-close-core.md"
    refuse_ok = refuse.is_file() and "precedence" in refuse.read_text(encoding="utf-8").lower()
    probe(
        findings,
        "BH-008",
        "High",
        "customer_coercion",
        "Refuse close-core runbook exists with precedence",
        refuse_ok,
        str(refuse),
    )

    # --- E: SKU files not falsely live ---
    sku_scan_live = 0
    for p in (REPO / "commercial" / "skus").rglob("*.md"):
        if "dry-run" in str(p):
            continue
        t = p.read_text(encoding="utf-8", errors="replace").lower()
        if "**status:**" in t and "live" in t and "not sold" not in t and "designed" not in t:
            sku_scan_live += 1
    probe(
        findings,
        "BH-009",
        "Critical",
        "reputation_fud_self",
        "No SKU falsely marked live/sold",
        sku_scan_live == 0,
        f"false_live_count={sku_scan_live}",
    )

    # --- Isolation runbook hard rules present ---
    iso = REPO / "commercial" / "ISOLATION_RUNBOOK.md"
    iso_ok = False
    if iso.is_file():
        it = iso.read_text(encoding="utf-8")
        iso_ok = "signing" in it.lower() and ("separate" in it.lower() or "isolation" in it.lower())
    probe(
        findings,
        "BH-010",
        "High",
        "customer_coercion",
        "Isolation runbook requires separate signing keys / isolation",
        iso_ok,
        str(iso),
    )

    # --- Pitch free-core precedence (placeholder on site source md) ---
    pitch = REPO / "docs/placeholders/capital/FUNDRAISE_PITCH_EXAMPLE.md"
    pitch_ok = False
    if pitch.is_file():
        pt = pitch.read_text(encoding="utf-8")
        pitch_ok = "precedence" in pt.lower() and "never" in pt.lower() and "paywall" in pt.lower()
    probe(
        findings,
        "BH-011",
        "Medium",
        "investor_capture",
        "Fundraise pitch example asserts free-core precedence / anti-paywall",
        pitch_ok,
        str(pitch),
    )

    # --- Live economics page: free core not SKU ---
    code, _, body = http_get("https://ttllms.com/economics")
    econ_ok = code == 200 and ("not the product sku" in body.lower() or "never the sku" in body.lower() or "free core" in body.lower())
    probe(
        findings,
        "BH-012",
        "Medium",
        "openwash",
        "Economics page states free core is not the billable SKU",
        econ_ok,
        f"status={code}",
    )

    high_fail = [f for f in findings if f["severity"] in ("Critical", "High") and not f["pass"]]
    out = {
        "schema": "ttllm.business_redteam.v1",
        "campaign_id": "BHA-2026-08-08",
        "utc": utc(),
        "framing": "black-hat lens constructive QA — not criminal instruction",
        "personas": [
            "investor_capture",
            "openwash",
            "free_rider",
            "customer_coercion",
            "reputation_fud",
            "single_human_kill",
            "verify_paywall",
        ],
        "results": findings,
        "boundary_scan": scan.to_dict(),
        "summary": {
            "total": len(findings),
            "passed": sum(1 for f in findings if f["pass"]),
            "failed": sum(1 for f in findings if not f["pass"]),
            "high_critical_failed": len(high_fail),
        },
        "all_high_pass": len(high_fail) == 0,
    }
    outp = REPO / "registers" / "redteam" / "campaign_BHA-2026-08-08.json"
    outp.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    print("WROTE", outp, file=sys.stderr)
    return 0 if out["all_high_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
