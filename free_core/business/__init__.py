"""Business-boundary integrity helpers (Domain 8) — attack surface for constructive black-hat QA."""
from .boundary_guard import (
    BoundaryScanResult,
    scan_boundary_document,
    scan_repo_for_close_core_claims,
    scan_sku_statuses,
    scan_site_business_claims,
)

__all__ = [
    "BoundaryScanResult",
    "scan_boundary_document",
    "scan_repo_for_close_core_claims",
    "scan_sku_statuses",
    "scan_site_business_claims",
]
