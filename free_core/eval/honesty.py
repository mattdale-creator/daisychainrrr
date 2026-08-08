"""Eval honesty template — capability claims must not outrun artefacts."""
from __future__ import annotations
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional


DEFAULT_NON_CLAIMS = [
    "Not frontier-competitive",
    "Not OLMo/LLM360 scale",
    "Not a substitute for multi-trillion production ttlink",
    "Not production HSM-rooted",
]


def build_honesty_pack(
    release_name: str,
    *,
    tasks_run: List[Dict[str, Any]],
    non_claims: Optional[List[str]] = None,
    tombstones: Optional[List[str]] = None,
    merkle_root: Optional[str] = None,
    notes: str = "",
) -> dict:
    return {
        "schema": "ttllm.eval_honesty.v1",
        "release": release_name,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tasks_run": tasks_run,
        "non_claims": list(non_claims or DEFAULT_NON_CLAIMS),
        "tombstones": list(tombstones or []),
        "merkle_root": merkle_root,
        "notes": notes,
        "ethos": "empty honesty beats soft tissue",
    }


def honesty_markdown(pack: dict) -> str:
    lines = [
        f"# Eval honesty — {pack.get('release')}",
        "",
        f"Generated: {pack.get('generated_utc')}",
        "",
        "## Tasks run",
        "",
    ]
    for t in pack.get("tasks_run") or []:
        lines.append(f"- **{t.get('name')}**: {t.get('result', 'n/a')} — {t.get('note', '')}")
    lines += ["", "## Explicit non-claims", ""]
    for c in pack.get("non_claims") or []:
        lines.append(f"- {c}")
    lines += ["", "## Tombstones", ""]
    for t in pack.get("tombstones") or []:
        lines.append(f"- {t}")
    if pack.get("merkle_root"):
        lines += ["", f"merkle_root: `{pack['merkle_root']}`"]
    if pack.get("notes"):
        lines += ["", "## Notes", "", pack["notes"]]
    lines += ["", "*Ethos: down to the bone.*", ""]
    return "\n".join(lines)
