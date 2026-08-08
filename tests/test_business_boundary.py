"""Real tests for free_core.business.boundary_guard + business attack surface."""
from pathlib import Path

from free_core.business.boundary_guard import (
    scan_boundary_document,
    scan_repo_for_close_core_claims,
    scan_sku_statuses,
    scan_site_business_claims,
    scan_text_for_forbidden,
)

REPO = Path(__file__).resolve().parents[1]


def test_boundary_document_ok():
    r = scan_boundary_document(REPO / "commercial" / "BOUNDARY.md")
    assert r.ok, r.findings


def test_sku_statuses_not_live():
    r = scan_sku_statuses(REPO / "commercial" / "skus")
    assert r.ok, [f.to_dict() for f in r.findings if f.severity in ("Critical", "High")]


def test_site_no_company_complete_lie():
    r = scan_site_business_claims(REPO / "site")
    high = [f for f in r.findings if f.severity in ("Critical", "High")]
    assert not high, [f.to_dict() for f in high]


def test_repo_scan_high_pass():
    r = scan_repo_for_close_core_claims(REPO)
    assert r.ok, [f.to_dict() for f in r.findings if f.severity in ("Critical", "High")][:10]


def test_forbidden_pattern_detects_endorsement():
    findings = scan_text_for_forbidden(
        Path("synthetic.md"),
        "We will paywall verification of all public claims for revenue.\n",
        allow_prohibited_context=False,
    )
    assert any("paywalled" in f.code or "paywall" in f.message.lower() for f in findings)


def test_prohibited_list_line_skipped():
    findings = scan_text_for_forbidden(
        Path("boundary.md"),
        "- Prohibited: Paywall on verifying a public-core claim\n",
        allow_prohibited_context=True,
    )
    assert findings == []
