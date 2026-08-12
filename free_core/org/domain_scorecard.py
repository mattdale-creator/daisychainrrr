"""Evidence-based master domain scorecard (Domains 1–10).

Probes on-disk artefacts. Does not fake entity, signed covenant, standing
red-team hire, or frontier scale. Nano shape + process bone only.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class DomainRow:
    number: int
    name: str
    status: str
    notes: str
    evidence: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def _repo_root(start: Path | None = None) -> Path:
    if start is None:
        start = Path.cwd()
    start = Path(start).resolve()
    for p in [start, *start.parents]:
        if (p / "docs" / "specs" / "artefacts").is_dir() or (p / "free_core").is_dir():
            return p
    return start


def _exists(root: Path, rel: str) -> bool:
    return (root / rel).exists()


def _count_md(root: Path, rel: str) -> int:
    p = root / rel
    if not p.is_dir():
        return 0
    return sum(1 for _ in p.rglob("*.md"))


def build_domain_scorecard(repo: Path | None = None) -> Dict[str, Any]:
    root = _repo_root(repo)
    art = root / "docs" / "specs" / "artefacts"
    rows: List[DomainRow] = []

    # 1 Governance
    g_files = [
        "docs/specs/artefacts/01/GOVERNANCE_CHARTER.md",
        "registers/decisions/LOG.md",
        "docs/specs/artefacts/01/MONTHLY_AUDIT_CHECKLIST.md",
    ]
    g_ok = sum(1 for f in g_files if _exists(root, f))
    rows.append(
        DomainRow(
            1,
            "Governance",
            "BONE-process" if g_ok >= 2 else "PARTIAL",
            "Charter + decision log + audit process; no board (entity T6 open)",
            [f for f in g_files if _exists(root, f)],
        )
    )

    # 2 Ownership
    o_files = [
        "docs/specs/artefacts/02/BENEFICIAL_OWNERSHIP.md",
        "docs/specs/artefacts/02/CAP_TABLE_SUMMARY.md",
        "docs/specs/artefacts/02/FUNDING_HISTORY_LOG.md",
    ]
    o_ok = sum(1 for f in o_files if _exists(root, f))
    rows.append(
        DomainRow(
            2,
            "Ownership/Funding",
            "PARTIAL" if o_ok >= 2 else "MISSING",
            "Founder disclosure packs present; $0 institutional; entity T6 open",
            [f for f in o_files if _exists(root, f)],
        )
    )

    # 3 Data — cards live under models/*/data/DATA_CARD.md
    data_cards: List[Path] = []
    if (root / "models").is_dir():
        data_cards = list((root / "models").glob("ttllm-nano*/data/DATA_CARD.md"))
        if not data_cards:
            data_cards = list((root / "models").glob("ttllm-nano*/cards/DATA_CARD.md"))
    rows.append(
        DomainRow(
            3,
            "Data governance",
            "MET-nano" if data_cards else "PARTIAL",
            f"DATA_CARDs on {len(data_cards)} nano tree(s); PG public-domain hashes",
            [str(p.relative_to(root)) for p in data_cards[:6]],
        )
    )

    # 4 Evaluation
    claim = _exists(root, "docs/specs/artefacts/04/PUBLIC_CLAIM_GATE.md")
    rows.append(
        DomainRow(
            4,
            "Evaluation",
            "BONE-honest" if claim else "PARTIAL",
            "Claim gate + honesty packs; no frontier capability claims",
            ["docs/specs/artefacts/04/PUBLIC_CLAIM_GATE.md"] if claim else [],
        )
    )

    # 5 Incidents
    play = _exists(root, "docs/specs/artefacts/05/INCIDENT_DISCLOSURE_POLICY.md")
    rows.append(
        DomainRow(
            5,
            "Incidents",
            "BONE-process" if play else "PARTIAL",
            "Policy + tabletop process; no real High severity yet",
            ["docs/specs/artefacts/05/INCIDENT_DISCLOSURE_POLICY.md"] if play else [],
        )
    )

    # 6 Compensation
    phil = _exists(root, "docs/specs/artefacts/06/COMPENSATION_PHILOSOPHY.md")
    rows.append(
        DomainRow(
            6,
            "Compensation",
            "PARTIAL" if phil else "MISSING",
            "Philosophy + band examples; no payroll (entity/hire gates)",
            ["docs/specs/artefacts/06/COMPENSATION_PHILOSOPHY.md"] if phil else [],
        )
    )

    # 7 Supply chain
    supply = _exists(root, "manifests/SUPPLY_LOCK.json") or _exists(
        root, "docs/specs/artefacts/07/DEPENDENCY_REGISTER.md"
    )
    rows.append(
        DomainRow(
            7,
            "Supply chain",
            "MET" if supply else "PARTIAL",
            "Dependency register / SUPPLY_LOCK current for free-core software",
            [
                p
                for p in (
                    "manifests/SUPPLY_LOCK.json",
                    "docs/specs/artefacts/07/DEPENDENCY_REGISTER.md",
                )
                if _exists(root, p)
            ],
        )
    )

    # 8 Boundary
    bound = _exists(root, "commercial/BOUNDARY.md")
    skus = list((root / "commercial" / "skus").glob("*.md")) if (root / "commercial" / "skus").is_dir() else []
    refuse = _exists(root, "commercial/REFUSE_RESPONSE.md")
    rows.append(
        DomainRow(
            8,
            "Boundary",
            "MET-pre-revenue" if bound and refuse else "PARTIAL",
            f"BOUNDARY + refuse + {len(skus)} SKU designs; selling=false",
            [
                p
                for p in (
                    "commercial/BOUNDARY.md",
                    "commercial/REFUSE_RESPONSE.md",
                    "commercial/PRE_REVENUE_OPERATING_PACK.md",
                )
                if _exists(root, p)
            ],
        )
    )

    # 9 Stewardship
    cov = _exists(root, "docs/specs/artefacts/09/CONTINUITY_COVENANT.md") or _exists(
        root, "continuity"
    )
    rows.append(
        DomainRow(
            9,
            "Stewardship",
            "PARTIAL" if cov else "MISSING",
            "Draft covenant / continuity inventory; unsigned (T5/T6/T9 open)",
            [
                p
                for p in (
                    "docs/specs/artefacts/09/CONTINUITY_COVENANT.md",
                    "docs/specs/artefacts/09/PUBLIC_CORE_ASSET_INVENTORY.md",
                )
                if _exists(root, p)
            ],
        )
    )

    # 10 Red-team
    harness = _exists(root, "scripts/redteam_nano_harness.py")
    reg = _exists(root, "registers/redteam/FINDINGS_REGISTER.md")
    rows.append(
        DomainRow(
            10,
            "Red-team publication",
            "BONE-process" if harness and reg else "PARTIAL",
            "Harness + campaigns published; standing hire is hard gate T10",
            [
                p
                for p in (
                    "scripts/redteam_nano_harness.py",
                    "registers/redteam/FINDINGS_REGISTER.md",
                    "docs/security/TESTING_LOOP.md",
                )
                if _exists(root, p)
            ],
        )
    )

    return {
        "schema": "ttllm.domain_scorecard.v1",
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo": str(root),
        "artefact_md_count": _count_md(root, "docs/specs/artefacts"),
        "domains": [r.to_dict() for r in rows],
        "tombstones": [
            "No 32B / multi-trillion TTLLM",
            "No production multi-trillion ttlink index",
            "No entity / signed covenant / standing RT hire",
            "Nano shape only — not OLMo-class",
        ],
        "ethos": {
            "free_public_core_never_paywalled": True,
            "hard_gates_not_faked": True,
            "nano_is_not_frontier": True,
        },
    }


def scorecard_markdown(card: Dict[str, Any] | None = None, repo: Path | None = None) -> str:
    if card is None:
        card = build_domain_scorecard(repo)
    lines = [
        "# Master domain scorecard — project",
        f"Generated: {card['utc']}",
        "",
        "| # | Domain | Status | Notes |",
        "|---|--------|--------|-------|",
    ]
    for d in card["domains"]:
        lines.append(
            f"| {d['number']} | {d['name']} | {d['status']} | {d['notes']} |"
        )
    lines += [
        "",
        "## Tombstones",
    ]
    for t in card.get("tombstones") or []:
        lines.append(f"- {t}")
    lines += [
        "",
        f"Artefact markdown files under docs/specs/artefacts: **{card.get('artefact_md_count', '?')}**",
        "",
        "Machine source: `free_core.org.domain_scorecard` · regenerate: `python3 scripts/domain_scorecard_all.py`",
        "",
        "*Down to the bone.*",
        "",
    ]
    return "\n".join(lines)


def write_master_scorecard(repo: Path | None = None) -> Tuple[Path, Dict[str, Any]]:
    root = _repo_root(repo)
    card = build_domain_scorecard(root)
    out = root / "docs" / "specs" / "artefacts" / "MASTER_DOMAIN_SCORECARD.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(scorecard_markdown(card, root), encoding="utf-8")
    return out, card
