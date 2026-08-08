# 05-business/gtm-deep/contributor-ladder-empty/owner.md · owner

**Path:** `eventualities/05-business/gtm-deep/contributor-ladder-empty/owner.md`  
**Updated:** 2026-08-08  
**Leaf type:** owner — who is accountable

## Purpose
Who is accountable for: **component** · failure · phase before public release or claim · actor project lead / founder.

## Accountability
| Role | Responsibility |
|------|----------------|
| Primary | Project lead (md@0265.au) until free-core / Domain custodian hired |
| Technical | Whoever last sealed the related release (must document in decision log) |
| Security | Domain 5 / red-team owner for integrity threats |
| Commercial | Domain 8 boundary custodian if SKU pressure involved |

## RACI (bootstrap)
- **R**esponsible: primary above  
- **A**ccountable: project lead  
- **C**onsulted: any red-team / legal when High+  
- **I**nformed: public via scorecard/tombstone when free core affected  

## Vacancy rule
If primary is unavailable, succession notes in Domain 9 continuity inventory apply; do not leave this path ownerless.


## Artefacts / tools
- Paths: `see parent README`
- Registers: registers/incidents/ or registers/decisions/ as appropriate
- Verify suite: `scripts/oneshot_verify_all.py`, `scripts/redteam_nano_harness.py`

## Done when
- [x] Written procedure exists (this file)
- [ ] Owner has executed once (drill or real)
- [ ] Linked failure mode cannot recur without detection

## Related
Parent node README; `docs/specs/`; `commercial/BOUNDARY.md`; `STATUS_HONEST.md`
