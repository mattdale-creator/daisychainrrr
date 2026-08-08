#!/usr/bin/env python3
"""Build honest nano cost ledger from metrics (unit economics bone)."""
from __future__ import annotations
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def dir_bytes(p: Path) -> int:
    if not p.exists():
        return 0
    if p.is_file():
        return p.stat().st_size
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file())


def ledger_for(model: str, watts: float = 20.0) -> str:
    root = REPO / "models" / model
    hyp_p = root / "metrics" / "hyperparams.json"
    hyp = json.loads(hyp_p.read_text()) if hyp_p.exists() else {}
    wall = float(hyp.get("wall_sec") or 0)
    kwh = (wall * watts) / 3600.0 / 1000.0 if wall else 0.0
    ckpt = dir_bytes(root / "checkpoints")
    data = dir_bytes(root / "data")
    code = dir_bytes(root / "code")
    utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        f"# Cost ledger — {model}",
        "",
        f"**Generated:** {utc}",
        "",
        "| Item | Value |",
        "|------|-------|",
        f"| Device | {hyp.get('device', 'unknown')} |",
        f"| Steps | {hyp.get('steps', '—')} |",
        f"| Wall seconds | {wall:.1f} |",
        f"| Est. energy @{watts:g}W | {kwh:.4f} kWh |",
        f"| Checkpoint storage bytes | {ckpt:,} |",
        f"| Data tree bytes | {data:,} |",
        f"| Code tree bytes | {code:,} |",
        "| Cloud GPU invoice | $0 (local) |",
        "| Data license cost | $0 (public domain PG where used) |",
        "",
        "## Honesty",
        "This ledger is the actual cost of the nano demonstration.",
        "It does **not** validate multi-million-dollar scale training quotes.",
        "Scale budgets: `docs/placeholders/capital/SCALE_BUDGET_FILLED_EXAMPLE.md` (Grok example).",
        "",
        "## Hyperparams tip",
        "```json",
        json.dumps({k: hyp.get(k) for k in ("steps", "n_layer", "n_embd", "seed", "device", "corpus_sha256") if k in hyp}, indent=2),
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", action="append", default=None)
    ap.add_argument("--watts", type=float, default=20.0)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    models = args.model or [
        n.name for n in sorted((REPO / "models").glob("ttllm-nano*")) if n.is_dir()
    ]
    for m in models:
        text = ledger_for(m, watts=args.watts)
        out = REPO / "models" / m / "metrics" / "cost_ledger.md"
        if args.write:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text + "\n", encoding="utf-8")
            print("wrote", out)
        else:
            print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
