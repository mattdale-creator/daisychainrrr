# ttlink · scale-overclaim · pre-release · prevent

**Path:** `eventualities/cross-product/ttlink/scale-overclaim/pre-release/prevent.md`  
**Updated:** 2026-08-08  
**Leaf type:** prevent — controls that stop recurrence

## Purpose
Controls that stop recurrence for: **ttlink** · capability or corpus scale is overstated relative to artefacts · phase before public release or claim · actor project lead / founder.

## Preventive controls
1. **Release gate:** checklist requires this layer/artefact healthy or explicitly tombstoned before “TTLLM” claims.
2. **Automation:** prefer scripts (`oneshot_verify_all`, redteam harness, manifest verify) over memory.
3. **BOUNDARY:** commercial SKUs cannot require opacity here if free-core (`commercial/BOUNDARY.md`).
4. **Cadence:** monthly decision-log audit; quarterly domain report (`docs/specs/artefacts/*/QUARTERLY_REPORT_TEMPLATE.md`).
5. **Access:** least-privilege tokens; secrets never in git (`ops/HUMAN_GATES.md` for scope gaps).
6. **Culture:** reward finding gaps; punish silent cover-ups (“remember you’re on drugs”).

## Design rule
If a control is not written here and not automated, assume it will fail under pressure.


## Artefacts / tools
- Paths: `models/*/ttlink/ + free_core/ttlink`
- Registers: registers/incidents/ + redteam
- Verify suite: `scripts/oneshot_verify_all.py`, `scripts/redteam_nano_harness.py`

## Done when
- [x] Written procedure exists (this file)
- [ ] Owner has executed once (drill or real)
- [ ] Linked failure mode cannot recur without detection

## Related
Parent node README; `docs/specs/`; `commercial/BOUNDARY.md`; `STATUS_HONEST.md`
