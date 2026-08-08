# Domain 3 — Data governance & legal response (human handbook)

**Updated:** 2026-08-08  
**Owner (R/A):** project lead; Legal Response Owner when staffed  
**Normative:** `docs/specs/03-data-governance.md`  
**Artefacts:** `docs/specs/artefacts/03/`  
**Registers:** `registers/legal/LEGAL_ACTION_LOG.md`, `registers/legal/DATA_CHANGE_LOG.md`

## Purpose
Public training data is free-core bone. Changes and legal pressure must be visible (tombstone > silent delete).

## Procedure — prepare / document a training corpus (nano)

1. Prefer public-domain / clearly licensed sources (current: Project Gutenberg).
2. Run (example nano):
```bash
python3 models/ttllm-nano/code/prepare_data.py
# or ensure models/*/data/processed/sources.json + DATA_CARD.md exist
```
3. Confirm each source has: URL, license, full_sha256, trainslice_sha256.
4. Read `models/<release>/data/DATA_CARD.md` for human summary.
5. Append data change to `registers/legal/DATA_CHANGE_LOG.md` if mixture changes after a public seal.

## Procedure — legal demand / takedown intake

1. **Same day:** record receipt internally; do not silently alter public artefacts.
2. Within **14 days** if public artefacts affected: add row to `registers/legal/LEGAL_ACTION_LOG.md`:
   - ID, date received, nature (no secrets/PII beyond need), artefacts affected, decision, rationale, restored?
3. Default: **preserve** public data; removal is exceptional.
4. Prefer **tombstone** (what removed, why, prior hash) over silent deletion — see `docs/specs/artefacts/03/TOMBSTONE_STANDARD.md`.
5. If legal basis later falls away: **restore** and log (`RESTORATION_BIAS.md`).
6. Informal pressure that changes data is treated like formal process (same log).
7. Update scorecards; stream event `data_change` or `tombstone` if public core affected.
8. Domain 1 decision if policy changes.

## Severity / timeline
| Event | Timeline |
|-------|----------|
| Intake record | Day of receipt |
| Public log if artefacts changed | ≤14 days |
| Restoration when basis ends | Prompt; log same week |

## Commands
```bash
ls models/ttllm-nano/data/processed/
cat models/ttllm-nano/data/DATA_CARD.md | head -40
ls registers/legal/
python3 -m free_core.provenance.cli verify --manifest models/ttllm-nano/manifests/RELEASE_MANIFEST.json --base models/ttllm-nano
```

## RACI
| Role | Duty |
|------|------|
| Data Governance Lead | Cards, mixture, change log |
| Legal Response Owner | Legal action log accuracy |
| Technical custodian | Implement exact logged changes + re-seal |

## Done when
- [x] Policy + logs exist
- [x] Nano DATA_CARDs with hashes
- [ ] First real legal demand handled under this process (none yet)
