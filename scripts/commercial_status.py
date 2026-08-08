#!/usr/bin/env python3
"""Publish commercial / business surface status (pre-revenue honest).

Writes site/demo/commercial_status.json (volatile — not sealed).
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core import __version__  # noqa: E402
from free_core.business.sku_catalog import load_sku_catalog  # noqa: E402
from free_core.business.boundary_guard import (  # noqa: E402
    scan_boundary_document,
    scan_sku_statuses,
    scan_site_business_claims,
    scan_repo_for_close_core_claims,
)


def build() -> dict:
    cat = load_sku_catalog(REPO)
    bound = scan_boundary_document(REPO / "commercial" / "BOUNDARY.md")
    skus = scan_sku_statuses(REPO / "commercial" / "skus")
    site = scan_site_business_claims(REPO / "site")
    repo_scan = scan_repo_for_close_core_claims(REPO)

    refuse = REPO / "commercial" / "REFUSE_RESPONSE.md"
    pre = REPO / "commercial" / "PRE_REVENUE_OPERATING_PACK.md"

    all_ok = bool(
        cat["integrity"]["ok"]
        and bound.ok
        and skus.ok
        and site.ok
        and repo_scan.ok
    )

    return {
        "schema": "ttllm.commercial_status.v1",
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "free_core_version": __version__,
        "pre_revenue": True,
        "selling": False,
        "ethos": {
            "free_public_core_never_paywalled": True,
            "monetise_outside_core": True,
            "product_is_the_proof": True,
            "no_fake_invoices": True,
        },
        "contact": "md@0265.au",
        "sku_catalog": cat,
        "boundary_scan": bound.to_dict(),
        "sku_status_scan": skus.to_dict(),
        "site_scan": site.to_dict(),
        "repo_close_core_scan": {
            "ok": repo_scan.ok,
            "finding_count": len(repo_scan.findings),
            "high_critical": sum(
                1 for f in repo_scan.findings if f.severity in ("Critical", "High")
            ),
        },
        "artefacts": {
            "boundary": "commercial/BOUNDARY.md",
            "isolation": "commercial/ISOLATION_RUNBOOK.md",
            "refuse_response": "commercial/REFUSE_RESPONSE.md" if refuse.is_file() else None,
            "pre_revenue_pack": "commercial/PRE_REVENUE_OPERATING_PACK.md" if pre.is_file() else None,
            "go_live_handbook": "docs/handbook/commercial/03-sku-go-live.md",
            "site": "site/commercial.html",
        },
        "all_ok": all_ok,
        "tombstone": (
            "SKUs are designed / not sold. First sale requires T6+T7+T11 "
            "and docs/handbook/commercial/03-sku-go-live.md checklist."
        ),
    }


def main() -> int:
    proof = build()
    out = REPO / "site" / "demo" / "commercial_status.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(proof, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "all_ok": proof["all_ok"],
                "pre_revenue": proof["pre_revenue"],
                "selling": proof["selling"],
                "sku_count": proof["sku_catalog"]["sku_count"],
                "integrity": proof["sku_catalog"]["integrity"],
                "wrote": str(out.relative_to(REPO)),
            },
            indent=2,
        )
    )
    return 0 if proof["all_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
