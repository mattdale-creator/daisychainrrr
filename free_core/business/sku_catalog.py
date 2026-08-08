"""Machine-readable commercial SKU catalog (Domain 8).

Founding paid layers live *outside* free public core. Every SKU is
**designed / not sold** until entity + KYC + real counterparty (T6/T7/T11).
This module is product-of-proof for the business surface — not a fake shop.
"""
from __future__ import annotations
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


# Founding six paid layers (turn 18) — filenames under commercial/skus/
SKU_FILES = (
    "hosted-infra.md",
    "enterprise-ttlink.md",
    "certified-finetunes.md",
    "analysis-workbench.md",
    "priority-support.md",
    "taas-methodology.md",
)

STATUS_DESIGNED = "designed / not sold"
STATUS_LIVE_FORBIDDEN_WITHOUT_GATES = re.compile(
    r"\*\*Status:\*\*\s*(live|sold|shipping|ga)\b", re.I
)


@dataclass
class Sku:
    id: str
    path: str
    title: str
    status: str
    problem: str
    pays_for: str
    free_core_unaffected: bool
    designed_not_sold: bool
    live_claim: bool
    hard_gates_before_sale: List[str] = field(
        default_factory=lambda: ["T6_entity", "T7_bank_kyc", "T11_first_revenue_counterparty"]
    )

    def to_dict(self) -> dict:
        return asdict(self)


def _repo_root(start: Path | None = None) -> Path:
    if start is None:
        start = Path.cwd()
    start = Path(start).resolve()
    for p in [start, *start.parents]:
        if (p / "commercial" / "BOUNDARY.md").is_file() or (p / "free_core").is_dir():
            return p
    return start


def _section(text: str, heading: str) -> str:
    # ## Heading ... until next ##
    m = re.search(
        rf"^##\s+{re.escape(heading)}\s*\n(.*?)(?=^##\s+|\Z)",
        text,
        re.I | re.M | re.S,
    )
    if not m:
        return ""
    return m.group(1).strip()


def parse_sku_file(path: Path, *, repo: Path | None = None) -> Sku:
    text = path.read_text(encoding="utf-8", errors="replace")
    title_m = re.search(r"^#\s+SKU:\s*(.+)$", text, re.M)
    title = (title_m.group(1).strip() if title_m else path.stem)
    status_m = re.search(r"\*\*Status:\*\*\s*(.+)$", text, re.M)
    status = (status_m.group(1).strip() if status_m else "unknown")
    live = bool(STATUS_LIVE_FORBIDDEN_WITHOUT_GATES.search(text))
    designed = bool(re.search(r"designed\s*/\s*not sold|not sold", status, re.I))
    problem = _section(text, "Problem").split("\n")[0] if _section(text, "Problem") else ""
    pays = _section(text, "What customer pays for")
    free_ok = bool(re.search(r"Free core unaffected|free public core remains free", text, re.I))
    rel = str(path.resolve().relative_to(repo.resolve())) if repo else str(path.as_posix())
    return Sku(
        id=path.stem,
        path=rel,
        title=title,
        status=status,
        problem=problem[:240],
        pays_for=pays[:400],
        free_core_unaffected=free_ok,
        designed_not_sold=designed,
        live_claim=live,
    )


def load_sku_catalog(repo: Path | None = None) -> Dict[str, Any]:
    root = _repo_root(repo)
    skus_dir = root / "commercial" / "skus"
    skus: List[Sku] = []
    missing: List[str] = []
    for name in SKU_FILES:
        p = skus_dir / name
        if not p.is_file():
            missing.append(name)
            continue
        skus.append(parse_sku_file(p, repo=root))

    false_live = [s for s in skus if s.live_claim]
    not_honest = [s for s in skus if not s.designed_not_sold and not s.live_claim]
    boundary = root / "commercial" / "BOUNDARY.md"
    isolation = root / "commercial" / "ISOLATION_RUNBOOK.md"
    refuse = root / "docs" / "handbook" / "commercial" / "02-refuse-close-core.md"

    ok = (
        len(missing) == 0
        and len(false_live) == 0
        and all(s.designed_not_sold for s in skus)
        and all(s.free_core_unaffected for s in skus)
        and boundary.is_file()
    )

    return {
        "schema": "ttllm.sku_catalog.v1",
        "ethos": {
            "free_public_core_never_paywalled": True,
            "paid_layers_outside_core": True,
            "designed_not_sold_until_hard_gates": True,
            "revenue_is_t11": True,
        },
        "pre_revenue": True,
        "contact": "md@0265.au",
        "boundary": "commercial/BOUNDARY.md",
        "isolation": "commercial/ISOLATION_RUNBOOK.md" if isolation.is_file() else None,
        "refuse_handbook": str(refuse.relative_to(root)) if refuse.is_file() else None,
        "sku_count": len(skus),
        "skus": [s.to_dict() for s in skus],
        "missing_files": missing,
        "false_live_claims": [s.id for s in false_live],
        "integrity": {
            "ok": ok,
            "all_designed_not_sold": all(s.designed_not_sold for s in skus) and not false_live,
            "all_state_free_core_unaffected": all(s.free_core_unaffected for s in skus),
            "boundary_present": boundary.is_file(),
        },
        "hard_gates_before_first_sale": [
            "T6 — legal entity",
            "T7 — bank / payment KYC",
            "T11 — real customer signature + payment",
        ],
        "allowed_pre_revenue_work": [
            "Publish BOUNDARY and SKU designs",
            "Refuse close-core asks with public template",
            "Dry-run go-live checklists",
            "Collect interest at md@0265.au without selling exclusive bone",
            "Keep free-core verify unpaid",
        ],
    }


def catalog_ok(repo: Path | None = None) -> bool:
    return bool(load_sku_catalog(repo)["integrity"]["ok"])
