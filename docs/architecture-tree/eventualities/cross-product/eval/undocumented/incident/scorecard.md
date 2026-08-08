# eval · undocumented · incident · scorecard

**Path:** `eventualities/cross-product/eval/undocumented/incident/scorecard.md`  
**Updated:** 2026-08-08  
**Leaf type:** scorecard — how scorecards/tombstones must reflect this

## Purpose
How scorecards/tombstones must reflect this for: **eval** · artefact exists without public procedure, card, or scorecard row · phase during or after a known incident · actor project lead / founder.

## Scorecard rules
1. Cannot mark **MET** for related domain/layer if this eventuality is active without remediation.
2. If incomplete by design (e.g. nano scale), mark **TOMBSTONE** with plain-language limit — never silent.
3. Update:
   - `models/*/cards/TRANSPARENCY_SCORECARD.md` for model releases
   - `docs/specs/artefacts/MASTER_DOMAIN_SCORECARD.md` for org domains
4. Re-run `python3 scripts/domain_scorecard_all.py` after changes.

## Example rows
| Status | When |
|--------|------|
| MET | Verify green; artefact present; claim matches bone |
| PARTIAL | Bootstrap only; staffed process incomplete |
| TOMBSTONE | Intentionally not shipped (e.g. not 32B) with public note |


## Artefacts / tools
- Paths: `models/*/evals/`
- Registers: registers/decisions/ if claim involved
- Verify suite: `scripts/oneshot_verify_all.py`, `scripts/redteam_nano_harness.py`

## Done when
- [x] Written procedure exists (this file)
- [ ] Owner has executed once (drill or real)
- [ ] Linked failure mode cannot recur without detection

## Related
Parent node README; `docs/specs/`; `commercial/BOUNDARY.md`; `STATUS_HONEST.md`
