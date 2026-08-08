# contradicts-BOUNDARY · d01 · charter · respond

**Path:** `eventualities/domain-artefact-failures/d01/charter/contradicts-BOUNDARY/respond.md`  
**Updated:** 2026-08-08  
**Leaf type:** respond — exact steps after detection

## Purpose
Exact steps after detection for: Domain 01 artefact **charter** under threat **practice or SKU contradicts commercial/BOUNDARY.md**.

## Response procedure (do in order)
1. **Halt soft tissue:** remove or correct any public claim that assumes this path is healthy.
2. **Open a log entry** in registers/ + docs/specs/artefacts/01/ the same day for material issues (Domain 5: High/Critical ack within 72h).
3. **Contain:** identify last good sealed tag/commit; do not force-push secrets or fake history.
4. **Remediate:**
   - Restore or regenerate artefact under `docs/specs/artefacts/01/, docs/specs/01-*.md`
   - Re-seal: `seal_model_tree` / `ttllm-manifest seal-repo` / model seal scripts
   - Fix BOUNDARY/commercial if pressure caused the break (Domain 8)
5. **Disclose honestly:** tombstone if incomplete; update scorecards; optional stream event.
6. **Verify green:** re-run oneshot_verify_all + relevant unit tests.
7. **Close** only with honest scorecard row (MET or TOMBSTONE, never silent).

## Communications
- Internal: owner + project lead
- External: only facts supported by seals; no capability cosplay


## Artefacts / tools
- Paths: `docs/specs/artefacts/01/, docs/specs/01-*.md`
- Registers: registers/ + docs/specs/artefacts/01/
- Verify suite: `scripts/oneshot_verify_all.py`, `scripts/redteam_nano_harness.py`

## Done when
- [x] Written procedure exists (this file)
- [ ] Owner has executed once (drill or real)
- [ ] Linked failure mode cannot recur without detection

## Related
Parent node README; `docs/specs/`; `commercial/BOUNDARY.md`; `STATUS_HONEST.md`
