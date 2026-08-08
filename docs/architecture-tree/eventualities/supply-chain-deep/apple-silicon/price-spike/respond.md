# price-spike · apple-silicon · respond

**Path:** `eventualities/supply-chain-deep/apple-silicon/price-spike/respond.md`  
**Updated:** 2026-08-08  
**Leaf type:** respond — exact steps after detection

## Purpose
Exact steps after detection for: Supply dependency **apple-silicon** risk **cost change threatens free-core hosting**.

## Response procedure (do in order)
1. **Halt soft tissue:** remove or correct any public claim that assumes this path is healthy.
2. **Open a log entry** in registers/supply-chain/ + registers/incidents/ the same day for material issues (Domain 5: High/Critical ack within 72h).
3. **Contain:** identify last good sealed tag/commit; do not force-push secrets or fake history.
4. **Remediate:**
   - Restore or regenerate artefact under `registers/supply-chain/DEPENDENCY_REGISTER.md`
   - Re-seal: `seal_model_tree` / `ttllm-manifest seal-repo` / model seal scripts
   - Fix BOUNDARY/commercial if pressure caused the break (Domain 8)
5. **Disclose honestly:** tombstone if incomplete; update scorecards; optional stream event.
6. **Verify green:** re-run oneshot_verify_all + relevant unit tests.
7. **Close** only with honest scorecard row (MET or TOMBSTONE, never silent).

## Communications
- Internal: owner + project lead
- External: only facts supported by seals; no capability cosplay


## Artefacts / tools
- Paths: `registers/supply-chain/DEPENDENCY_REGISTER.md`
- Registers: registers/supply-chain/ + registers/incidents/
- Verify suite: `scripts/oneshot_verify_all.py`, `scripts/redteam_nano_harness.py`

## Done when
- [x] Written procedure exists (this file)
- [ ] Owner has executed once (drill or real)
- [ ] Linked failure mode cannot recur without detection

## Related
Parent node README; `docs/specs/`; `commercial/BOUNDARY.md`; `STATUS_HONEST.md`
