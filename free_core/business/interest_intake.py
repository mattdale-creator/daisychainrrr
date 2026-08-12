"""Pre-revenue interest intake classifier (Domain 8).

Classifies inbound email/message text into honest paths without issuing
invoices or faking sales (T6/T7/T11 remain open). Product is the proof:
refuse close-core, capture paid-layer interest only, point funders at T8,
and route verify requests to unpaid public_proof.
"""
from __future__ import annotations
import re
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple


PATH_REFUSE_CLOSE_CORE = "refuse_close_core"
PATH_COMMERCIAL_INTEREST = "commercial_interest_only"
PATH_FUND_SCALE = "fund_scale_hard_gate"
PATH_VERIFY = "verify_unpaid"
PATH_GENERAL = "general_inquiry"
PATH_EMPTY = "empty"

# Close-core / exclusive bone asks → refuse template
_CLOSE_CORE: Tuple[re.Pattern[str], ...] = (
    re.compile(r"\bpaywall\b.{0,40}\bverif", re.I),
    re.compile(r"\bexclusive\b.{0,30}\b(weights?|free[- ]?core|public\s+core|bone)\b", re.I),
    re.compile(r"\bclose\b.{0,20}\b(the\s+)?(free\s+)?core\b", re.I),
    re.compile(r"\bprivatise\b|\bprivatize\b", re.I),
    re.compile(r"\bnever\s+publish\b.{0,30}\b(weights?|data|manifests?)\b", re.I),
    re.compile(r"\bonly\s+paying\s+(customers?|clients?)\b.{0,40}\b(weights?|access)\b", re.I),
    re.compile(r"\bremove\b.{0,20}\bpublic\s+(core|weights?|checkpoints?)\b", re.I),
)

# Paid layers outside core → interest only (not a sale)
_COMMERCIAL: Tuple[re.Pattern[str], ...] = (
    re.compile(r"\bhosted\b.{0,20}\b(infra|sla|uptime)\b", re.I),
    re.compile(r"\benterprise\b.{0,20}\bttlink\b", re.I),
    re.compile(r"\bfine[- ]?tune\b|\bcertified\b", re.I),
    re.compile(r"\bworkbench\b|\bpriority\s+support\b", re.I),
    re.compile(r"\bTaaS\b|\bmethodology\b|\baudit\s+tool", re.I),
    re.compile(r"\bwe\s+want\s+to\s+buy\b|\bpurchase\b|\blicense\b|\bMSA\b|\bSOW\b", re.I),
    re.compile(r"\bSLA\b|\bdedicated\b.{0,20}\b(cluster|instance)\b", re.I),
)

# Scale / capital → hard gate T8
_FUND: Tuple[re.Pattern[str], ...] = (
    re.compile(r"\binvest\b|\binvestment\b|\bfundraise\b|\bseries\s*[a-c]\b", re.I),
    re.compile(r"\b32\s*B\b|\btrillion\b|\btrain\s+(at\s+)?scale\b|\bGPU\s+cluster\b", re.I),
    re.compile(r"\bterm\s+sheet\b|\bseed\s+round\b|\bcheck\s+size\b", re.I),
)

# Verify / proof → unpaid path
_VERIFY: Tuple[re.Pattern[str], ...] = (
    re.compile(r"\bverif(y|ication)\b|\bpublic_proof\b|\bmerkle\b|\bttlink\b", re.I),
    re.compile(r"\breproduce\b|\bre[- ]?run\b|\bchecksum\b|\bseal\b", re.I),
    re.compile(r"\bhow\s+do\s+I\s+(check|prove|audit)\b", re.I),
)


@dataclass
class InterestVerdict:
    path: str
    severity: str  # refuse | capture | hard_gate | help | ignore
    title: str
    action: str
    artefact: str
    matched: List[str] = field(default_factory=list)
    pre_revenue: bool = True
    selling: bool = False
    hard_gates: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def _hits(patterns: Sequence[re.Pattern[str]], text: str) -> List[str]:
    out: List[str] = []
    for rx in patterns:
        m = rx.search(text)
        if m:
            out.append(m.group(0)[:80])
    return out


def classify_interest(text: str) -> InterestVerdict:
    """Classify a single inbound message body (or subject+body)."""
    raw = (text or "").strip()
    if not raw:
        return InterestVerdict(
            path=PATH_EMPTY,
            severity="ignore",
            title="Empty message",
            action="No action.",
            artefact="",
        )

    close = _hits(_CLOSE_CORE, raw)
    if close:
        return InterestVerdict(
            path=PATH_REFUSE_CLOSE_CORE,
            severity="refuse",
            title="Close-core / exclusive bone ask",
            action=(
                "Refuse. Free public core never paywalled or closed. "
                "Send commercial/REFUSE_RESPONSE.md template. Log material pressure."
            ),
            artefact="commercial/REFUSE_RESPONSE.md",
            matched=close,
            hard_gates=[],
        )

    fund = _hits(_FUND, raw)
    if fund:
        return InterestVerdict(
            path=PATH_FUND_SCALE,
            severity="hard_gate",
            title="Scale / capital interest",
            action=(
                "Do not claim a raise. Point to hard gate T8 and "
                "docs/placeholders/capital/. Free core stays public."
            ),
            artefact="docs/HARD_TECHNOLOGICAL_GATES.md",
            matched=fund,
            hard_gates=["T8_capital"],
        )

    commercial = _hits(_COMMERCIAL, raw)
    if commercial:
        return InterestVerdict(
            path=PATH_COMMERCIAL_INTEREST,
            severity="capture",
            title="Paid-layer interest (outside free core)",
            action=(
                "Capture as interest only. No invoice, SOW, or reserved capacity "
                "until T6 entity + T7 bank/KYC + T11 counterparty. "
                "Share commercial SKU one-pagers + BOUNDARY."
            ),
            artefact="commercial/PRE_REVENUE_OPERATING_PACK.md",
            matched=commercial,
            hard_gates=["T6_entity", "T7_bank_kyc", "T11_first_revenue_counterparty"],
        )

    verify = _hits(_VERIFY, raw)
    if verify:
        return InterestVerdict(
            path=PATH_VERIFY,
            severity="help",
            title="Verification / unpaid proof",
            action=(
                "Point to unpaid public proof: python3 scripts/public_proof.py, "
                "https://ttllms.com/demo, https://ttllms.com/status, GitHub clone."
            ),
            artefact="scripts/public_proof.py",
            matched=verify,
        )

    return InterestVerdict(
        path=PATH_GENERAL,
        severity="help",
        title="General inquiry",
        action=(
            "Reply from md@0265.au with BOUNDARY summary, free-core links, "
            "and commercial.html if relevant. Still pre-revenue."
        ),
        artefact="commercial/PRE_REVENUE_OPERATING_PACK.md",
    )


def classify_batch(messages: Sequence[str]) -> Dict[str, Any]:
    verdicts = [classify_interest(m).to_dict() for m in messages]
    counts: Dict[str, int] = {}
    for v in verdicts:
        counts[v["path"]] = counts.get(v["path"], 0) + 1
    refuse_n = counts.get(PATH_REFUSE_CLOSE_CORE, 0)
    return {
        "schema": "ttllm.interest_intake.v1",
        "pre_revenue": True,
        "selling": False,
        "count": len(verdicts),
        "path_counts": counts,
        "verdicts": verdicts,
        "integrity": {
            "ok": True,
            "no_auto_invoice": True,
            "refuse_close_core_supported": True,
            "refuse_hits": refuse_n,
        },
        "ethos": {
            "free_public_core_never_paywalled": True,
            "monetise_outside_core": True,
            "no_fake_invoices": True,
        },
    }


# Fixed demo corpus for site + tests (stable; no wall-clock)
DEMO_MESSAGES: Tuple[Tuple[str, str], ...] = (
    (
        "We will invest if you exclusive free-core weights for paying customers only.",
        PATH_REFUSE_CLOSE_CORE,
    ),
    (
        "Interested in hosted infra with SLA and enterprise ttlink tooling.",
        PATH_COMMERCIAL_INTEREST,
    ),
    (
        "Can we fund a 32B train at scale? Term sheet ready.",
        PATH_FUND_SCALE,
    ),
    (
        "How do I verify the Merkle seal and re-run public_proof unpaid?",
        PATH_VERIFY,
    ),
    (
        "Hello — what is TTLLM?",
        PATH_GENERAL,
    ),
)


def demo_corpus_ok() -> bool:
    for text, expected in DEMO_MESSAGES:
        if classify_interest(text).path != expected:
            return False
    return True
