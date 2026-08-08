"""Generate per-release transparency scorecard markdown."""
from __future__ import annotations
from datetime import datetime, timezone
from typing import List, Tuple

DomainScore = Tuple[str, str, str]  # name, status, notes


def build_scorecard(
    release_name: str,
    domains: List[DomainScore],
    tombstones: List[str],
    merkle_root: str | None = None,
) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        f"# Transparency scorecard — {release_name}",
        "",
        f"Generated: {now}",
        "",
        "| Domain | Status | Notes |",
        "|--------|--------|-------|",
    ]
    for name, status, notes in domains:
        lines.append(f"| {name} | {status} | {notes} |")
    lines += ["", "## Tombstones", ""]
    for t in tombstones:
        lines.append(f"- {t}")
    if merkle_root:
        lines += ["", f"merkle_root: `{merkle_root}`", ""]
    lines.append("*Ethos: down to the bone. Empty honesty beats soft tissue.*")
    return "\n".join(lines) + "\n"
