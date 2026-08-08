# Scale-up train (when capital exists)

**Updated:** 2026-08-08  
**Owner (R):** Training Lead (future)  
**Status:** **Documented deferred epoch** — not executable on founding Mac alone  
**Gates:** capital, entity, multi-party keys, Domain 1 decisions

## Purpose
Define the **honest path** from nano shape to larger public models (e.g. OLMo/LLM360 class ambition) without pretending capital already closed the gap.

## Non-negotiables (ethos)
1. Free public core remains free — weights, data mixture docs, checkpoints policy, train code, basic ttlink, manifests, public stream.
2. No paywall on verifying public claims.
3. Data governance (Domain 3) before first large run.
4. BOUNDARY reviewed if any commercial fine-tune path appears.
5. Scorecard tombstones until each claim is met with artefacts.

## Preconditions (human gates)
| Gate | Handbook | Why |
|------|----------|-----|
| Capital | fundraising + Domain 2 | GPU/cluster cost |
| Legal entity | [gates/04-entity-covenant](../gates/04-entity-covenant.md) | contracts, IP, keys |
| Production keys / HSM | Domain 9 | release signatures |
| Data mixture license pack | Domain 3 | train legality |
| Domain 1 decision | `registers/decisions/` | material scale commitment |

## Procedure outline (when funded)

### Phase A — Design freeze
1. Publish **model card draft** + **data mixture card** under free core.
2. Domain 1 decision: target size, budget, public release commitment.
3. Isolation: training infra identity ≠ commercial tenant infra.
4. Choose open stack (code paths published in repo; prefer reusable free_core seals).

### Phase B — Infra
1. Provision cluster (cloud or on-prem) with audit logging.
2. Separate **signing** credentials from **train** credentials.
3. R2 / object store for public artefacts (see [gates/02-r2](../gates/02-r2.md)).
4. Canary documents in public corpus shards.

### Phase C — Train
1. Log stream events: `data_prepared`, `training_started`, periodic `loss_metric`, `checkpoint_saved`, `training_finished`.
2. Dense or schedule-defined public checkpoints — document interval.
3. No silent data swaps mid-run without Domain 3 process + stream note.

### Phase D — Seal & ship
1. Merkle manifests over weights, data docs, code pin, metrics.
2. ttlink index at feasible shard scale (tombstone multi-TB until real).
3. Eval pack with **honest** capability numbers + comparison table.
4. Full [01-ship-release](01-ship-release.md) path.
5. Public red-team invitation window (Domain 10).

## Commands (placeholders until stack chosen)
```bash
# After scale stack lands, replace with real entrypoints; keep verify surface stable:
python3 -m free_core.provenance.cli verify --manifest path/to/RELEASE_MANIFEST.json --base path/to/release
python3 -m free_core.stream.cli verify path/to/public_log.json
python3 scripts/domain_scorecard_all.py
```

## Forbidden until artefacts exist
- Claiming parity with OLMo/LLM360
- "Full transparency" without data mixture publication
- Investor narrative that free core will close later

## RACI (future org)
| Role | R | A | C | I |
|------|---|---|---|---|
| Training Lead | ✓ | | | |
| Project lead / board | | ✓ | | |
| Domain 3 Legal/Data | | | ✓ | |
| Domain 8 Boundary | | | ✓ | |
| Domain 10 Red-team | | | ✓ | |
| Public | | | | ✓ |

## Done when
- [ ] Capital + entity gates logged closed
- [ ] First large public run sealed + verified by third party
- [ ] Scorecard domains updated from TOMBSTONE → MET/PARTIAL with evidence

## Related
- Founding ambition: OLMo + LLM360 class transparency
- Gap audit: `docs/audits/GAP_AUDIT_vs_FOUNDING_TRANSCRIPT.md`
- Human gates: `ops/HUMAN_GATES.md`
