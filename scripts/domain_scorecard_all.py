#!/usr/bin/env python3
"""Emit master scorecard across domains for current project state."""
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
scores = [
    (1, "Governance", "PARTIAL", "Charter + decision log; no board"),
    (2, "Ownership/Funding", "PARTIAL", "100% founder disclosure; $0 institutional"),
    (3, "Data governance", "MET-nano", "DATA_CARDs + PG hashes + legal logs ready"),
    (4, "Evaluation", "PARTIAL", "Process eval packs only; no capability claims"),
    (5, "Incidents", "PARTIAL", "Policy + empty log"),
    (6, "Compensation", "PARTIAL", "Philosophy; no employees"),
    (7, "Supply chain", "MET", "Dependency register current"),
    (8, "Boundary", "MET-pre-revenue", "BOUNDARY.md + isolation runbook"),
    (9, "Stewardship", "PARTIAL", "Draft covenant unsigned"),
    (10, "Red-team publication", "PARTIAL", "Harness green; no standing team"),
]
lines = [
    "# Master domain scorecard — project",
    f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
    "",
    "| # | Domain | Status | Notes |",
    "|---|--------|--------|-------|",
]
for n, name, st, notes in scores:
    lines.append(f"| {n} | {name} | {st} | {notes} |")
lines += [
    "",
    "## Tombstones",
    "- No 32B / multi-trillion TTLLM",
    "- No production FM-index",
    "- No entity / signed covenant",
    "- Pages Function /api/ttlink may not route (static fallback) — client demo remains bone",
    "",
    "*Down to the bone.*",
]
out = ROOT / "docs/specs/artefacts/MASTER_DOMAIN_SCORECARD.md"
out.write_text("\n".join(lines) + "\n")
print("wrote", out)
