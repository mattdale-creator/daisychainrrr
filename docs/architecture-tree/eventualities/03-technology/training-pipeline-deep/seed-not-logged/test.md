# 03-technology/training-pipeline-deep/seed-not-logged/test.md · test

**Path:** `eventualities/03-technology/training-pipeline-deep/seed-not-logged/test.md`  
**Updated:** 2026-08-08  
**Leaf type:** test — how we verify the control works

## Purpose
How we verify the control works for: **component** · failure · phase before public release or claim · actor project lead / founder.

## Automated tests (run from repo root)
```bash
python3 -m pytest -q
python3 scripts/redteam_nano_harness.py
python3 scripts/oneshot_verify_all.py
# layer-specific examples:
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
python3 -m free_core.ttlink.cli canary-check --index models/ttllm-nano/ttlink/index.json
```

## Manual drill (tabletop)
1. Assume **failure** occurs in phase **before public release or claim** with actor **project lead / founder**.
2. Walk respond.md without looking at the answer key first.
3. Time-box 30–60 minutes; log gaps in the drill note under `registers/incidents/`.
4. Update this leaf if a step was impossible without tribal knowledge.

## Pass criteria
- Verify commands exit 0 (or failure is intentional and detected).
- Owner can execute without private chat history.
- Scorecard remains honest after the drill.


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
