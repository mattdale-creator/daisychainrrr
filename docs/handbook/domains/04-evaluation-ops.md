# Domain 4 — Evaluation operations (human handbook)

**Updated:** 2026-08-08  
**Owner (R/A):** project lead / Evaluation Lead when staffed  
**Normative:** `docs/specs/04-evaluation.md`  
**Gate:** `docs/specs/artefacts/04/PUBLIC_CLAIM_GATE.md`  
**Change log:** `docs/specs/artefacts/04/EVAL_CHANGE_LOG.md`

## Purpose
No public capability claim without published protocol, contamination honesty, and results linkage. Nano policy: **process evals only** — no frontier cosplay.

## Public claim gate (must pass before claiming capability)

1. Evaluation protocol version published (or explicit “process-only / no capability claim”).
2. Contamination analysis or residual uncertainty stated.
3. Raw results or pack linked to checkpoint hash.
4. Scorecard Domain 4 row honest.
5. See `PUBLIC_CLAIM_GATE.md`.

**Current nano releases:** do **not** make frontier capability claims. Use process packs:
- `models/ttllm-nano-v2/code/eval_pack.py` (BPE roundtrip, ttlink hits, loss/ppl)
- `models/*/evals/`

## Procedure — run process eval (nano-v2 example)

```bash
cd /path/to/daisychainrrr
python3 models/ttllm-nano-v2/code/eval_pack.py
# writes models/ttllm-nano-v2/evals/eval_pack.json
```

## Procedure — change evaluation methodology

1. Append `docs/specs/artefacts/04/EVAL_CHANGE_LOG.md`.
2. Domain 1 decision if it affects past public claims.
3. Re-run packs; re-seal model if release is public.
4. Update scorecard.

## Commands
```bash
python3 models/ttllm-nano-v2/code/eval_pack.py
python3 scripts/oneshot_verify_all.py
ls models/*/evals/
```

## RACI
Evaluation Lead R; release owner may not publish capability claims without Domain 4 artefacts.

## Done when
- [x] Process eval path documented
- [x] Public claim gate written
- [ ] First capability claim (if any) ships full protocol+contamination+results
