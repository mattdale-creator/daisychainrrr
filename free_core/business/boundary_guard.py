"""
Programmatic Boundary / business-claim integrity checks.

Hostile lens: investor capture, open-washing, paywalled verify, false SKU-live,
exclusive free-core language. Constructive QA — not a crime toolkit.
"""
from __future__ import annotations
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable, List, Optional


# Patterns a black-hat commercial actor would *want* true (we fail if we find them on free-core surface)
FORBIDDEN_CLAIM_PATTERNS = [
    (re.compile(r"paywall\w*\s+(to\s+)?verif", re.I), "paywalled_verification"),
    (re.compile(r"exclusive\s+(free[- ]?core|weights|public\s+core)", re.I), "exclusive_free_core"),
    (re.compile(r"close\s+the\s+(free\s+)?core", re.I), "close_the_core"),
    (re.compile(r"privatise\s+the\s+(free\s+)?(public\s+)?core", re.I), "privatise_core"),
    (re.compile(r"never\s+publish\s+(weights|data|manifests)", re.I), "never_publish_bone"),
    (re.compile(r"verification\s+only\s+(via|through)\s+paid", re.I), "verify_only_paid"),
    (re.compile(r"sold\s+exclusively\s+to\s+enterprise", re.I), "sold_exclusive_enterprise"),
]

# Required defenses in BOUNDARY.md
REQUIRED_BOUNDARY_MARKERS = [
    (re.compile(r"free public core", re.I), "free_public_core_named"),
    (re.compile(r"prohibited", re.I), "prohibited_section"),
    (re.compile(r"paywall", re.I), "paywall_word"),
    (re.compile(r"verif", re.I), "verification_word"),
    (re.compile(r"precedence|take precedence", re.I), "precedence"),
    (re.compile(r"side letter|investor", re.I), "investor_or_side_letter"),
]

# SKU status: hostile if claims live without entity/revenue honesty
SKU_LIVE_CLAIM = re.compile(r"\*\*Status:\*\*\s*(live|sold|shipping|ga)\b", re.I)
SKU_DESIGNED = re.compile(r"designed\s*/\s*not sold|not sold|status:\s*designed", re.I)


@dataclass
class Finding:
    code: str
    severity: str  # Critical | High | Medium | Low
    path: str
    message: str
    line: Optional[int] = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class BoundaryScanResult:
    ok: bool
    findings: List[Finding] = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "findings": [f.to_dict() for f in self.findings],
            "stats": self.stats,
        }


def _iter_text_files(root: Path, globs: Iterable[str]) -> List[Path]:
    out: List[Path] = []
    for g in globs:
        out.extend(root.glob(g))
    return sorted({p.resolve() for p in out if p.is_file()})


def scan_boundary_document(path: Path) -> BoundaryScanResult:
    findings: List[Finding] = []
    if not path.is_file():
        findings.append(Finding("BH-BOUND-MISSING", "Critical", str(path), "BOUNDARY.md missing"))
        return BoundaryScanResult(ok=False, findings=findings)
    text = path.read_text(encoding="utf-8", errors="replace")
    for rx, name in REQUIRED_BOUNDARY_MARKERS:
        if not rx.search(text):
            findings.append(
                Finding("BH-BOUND-MARKER", "High", str(path), f"Missing required marker: {name}")
            )
    # BOUNDARY itself may say "Paywall on verifying" as prohibited — that's OK
    # Only fail if it *endorses* paywall
    if re.search(r"must\s+paywall|shall\s+paywall|require\s+payment\s+to\s+verif", text, re.I):
        findings.append(
            Finding("BH-BOUND-ENDORSE", "Critical", str(path), "BOUNDARY appears to endorse paywalled verify")
        )
    return BoundaryScanResult(ok=len(findings) == 0, findings=findings, stats={"bytes": len(text)})


# Line is defensive (describes a prohibition/risk/non-goal) not an endorsement
_DEFENSIVE_MARKERS = (
    "prohibited",
    "forbid",
    "refuse",
    "must not",
    "shall not",
    "may not",
    "cannot ",
    "can't ",
    "never ",
    "nothing ",
    "without ",
    "not sold",
    "not buy",
    "never buy",
    "what they never",
    "tombstone",
    "hard gate",
    "do not",
    "don't ",
    "does not",
    "did not",
    "no sku",
    "no commercial",
    "non-goal",
    "non goal",
    "anti-paywall",
    "against ",
    "rejected",
    "void as",
    "force core closure",  # risk language
    "pressure to close",
    "closing the skeleton",
    "closing the core",
    "not allowed to buy",
    "is not allowed",
    "are not permitted",
    "not require",
    "without requiring",
    "remain free",
    "stays free",
    "stays public",
    "must remain free",
)


def _is_defensive_line(line: str) -> bool:
    low = line.lower()
    if any(m in low for m in _DEFENSIVE_MARKERS):
        return True
    # Markdown table "never buy" / non-goals columns often list forbidden phrases
    if low.strip().startswith("|") and low.count("|") >= 3:
        if any(
            x in low
            for x in (
                "non-goal",
                "never",
                "not ",
                "refuse",
                "forbidden",
                "exclusive free-core weights",  # in never-buy column of pitch
                "paywalled verification of public",
            )
        ):
            return True
    return False


def scan_text_for_forbidden(path: Path, text: str, *, allow_prohibited_context: bool = True) -> List[Finding]:
    """Scan free-text; skip lines/sections that list prohibitions, non-goals, or refuse language."""
    findings: List[Finding] = []
    section = ""
    defensive_section = False
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        # Track markdown / HTML headings for defensive sections
        if stripped.startswith("#") or re.match(r"^<h[1-4]\b", stripped, re.I):
            # strip md emphasis so "is *not* allowed" still matches
            section = re.sub(r"[*_`#]+", " ", stripped.lower())
            section = re.sub(r"\s+", " ", section)
            defensive_section = any(
                x in section
                for x in (
                    "forbid",
                    "prohib",
                    "reject",
                    "never ",
                    "not allow",
                    " is not ",
                    "not ttllm",
                    "must not",
                    "anti-",
                    "refuse",
                    "non-negotiable",
                    "what capital is not",
                    "what investors never",
                    "what they never",
                    "forbidden public claim",
                    "forbidden claim",
                    "tombstone",
                    "hard gate",
                    "out of scope",
                )
            )
        if allow_prohibited_context and (defensive_section or _is_defensive_line(line)):
            continue
        # Quoted forbidden examples e.g. "Enterprise customers get exclusive weights"
        if allow_prohibited_context and (
            (stripped.startswith("“") or stripped.startswith('"') or "“" in stripped[:3])
            and any(x in stripped.lower() for x in ("exclusive", "paywall", "only through paid"))
        ):
            continue
        for rx, code in FORBIDDEN_CLAIM_PATTERNS:
            if rx.search(line):
                findings.append(
                    Finding(
                        f"BH-CLAIM-{code}",
                        "High",
                        str(path),
                        f"Forbidden business claim pattern '{code}': {line.strip()[:160]}",
                        line=i,
                    )
                )
    return findings


def scan_sku_statuses(skus_dir: Path) -> BoundaryScanResult:
    findings: List[Finding] = []
    if not skus_dir.is_dir():
        findings.append(Finding("BH-SKU-DIR", "High", str(skus_dir), "commercial/skus missing"))
        return BoundaryScanResult(ok=False, findings=findings)
    count = 0
    live = 0
    for p in sorted(skus_dir.rglob("*.md")):
        if p.name.upper().startswith("README"):
            continue
        count += 1
        text = p.read_text(encoding="utf-8", errors="replace")
        if SKU_LIVE_CLAIM.search(text) and "not sold" not in text.lower() and "dry-run" not in str(p):
            live += 1
            findings.append(
                Finding(
                    "BH-SKU-LIVE",
                    "Critical",
                    str(p),
                    "SKU claims live/sold/GA without 'not sold' honesty — false revenue signal",
                )
            )
        elif not SKU_DESIGNED.search(text) and "dry-run" not in str(p).lower():
            # warn if no status line at all
            if "status" not in text.lower():
                findings.append(
                    Finding("BH-SKU-NOSTATUS", "Medium", str(p), "SKU missing status line")
                )
    return BoundaryScanResult(
        ok=not any(f.severity in ("Critical", "High") for f in findings),
        findings=findings,
        stats={"sku_files": count, "live_claims": live},
    )


def scan_site_business_claims(site_dir: Path) -> BoundaryScanResult:
    findings: List[Finding] = []
    if not site_dir.is_dir():
        return BoundaryScanResult(ok=False, findings=[Finding("BH-SITE", "High", str(site_dir), "site dir missing")])
    for p in sorted(site_dir.glob("*.html")):
        text = p.read_text(encoding="utf-8", errors="replace")
        findings.extend(scan_text_for_forbidden(p, text))
        # Soft-tissue: claim company complete without hard-gates mention on status-like pages
        if p.name in ("index.html", "status.html"):
            if re.search(r"\bcompany complete\b|\ball gates closed\b", text, re.I):
                findings.append(
                    Finding("BH-SITE-COMPLETE-LIE", "Critical", str(p), "Claims company complete / gates closed")
                )
    high = [f for f in findings if f.severity in ("Critical", "High")]
    return BoundaryScanResult(ok=len(high) == 0, findings=findings, stats={"pages": len(list(site_dir.glob('*.html')))})


def scan_repo_for_close_core_claims(repo: Path) -> BoundaryScanResult:
    """Scan commercial + site + pitch surfaces for hostile capture language."""
    findings: List[Finding] = []
    paths = _iter_text_files(
        repo,
        [
            "commercial/**/*.md",
            "site/*.html",
            "docs/business/*.md",
            "docs/placeholders/capital/*.md",
            "docs/placeholders/commercial/*.md",
            "STATUS_HONEST.md",
            "README.md",
        ],
    )
    for p in paths:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        # BOUNDARY.md and refuse docs list prohibited items — use allow context
        allow = "BOUNDARY" in p.name or "refuse" in p.name.lower() or "prohibited" in p.name.lower()
        # For BOUNDARY itself, only endorsement check via scan_boundary_document
        if p.name == "BOUNDARY.md":
            continue
        findings.extend(scan_text_for_forbidden(p, text, allow_prohibited_context=True))
    # Always include structural BOUNDARY + SKU scans
    b = scan_boundary_document(repo / "commercial" / "BOUNDARY.md")
    findings.extend(b.findings)
    s = scan_sku_statuses(repo / "commercial" / "skus")
    findings.extend(s.findings)
    site = scan_site_business_claims(repo / "site")
    findings.extend(site.findings)
    high = [f for f in findings if f.severity in ("Critical", "High")]
    return BoundaryScanResult(
        ok=len(high) == 0,
        findings=findings,
        stats={
            "files_scanned": len(paths),
            "boundary_ok": b.ok,
            "sku_ok": s.ok,
            "site_ok": site.ok,
            "high_findings": len(high),
        },
    )
