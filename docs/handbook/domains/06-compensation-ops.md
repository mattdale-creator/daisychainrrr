# Domain 6 — Compensation & incentives (human handbook)

**Updated:** 2026-08-08  
**Owner (R/A):** project lead / People lead when staffed  
**Normative:** `docs/specs/06-compensation.md`  
**Philosophy:** `docs/specs/artefacts/06/COMPENSATION_PHILOSOPHY.md`

## Purpose
Make incentive structure inspectable enough to detect anti-free-core pressure.

## Current state
Pre-headcount. No employees. Philosophy published. Bands deferred until first hire.

## Procedure — before first hire / sales role

1. Read `COMPENSATION_PHILOSOPHY.md`.
2. **Hard rule:** no commission or bonus that rewards closing or degrading free public core.
3. Publish role-level bands (`ROLE_BANDS_TEMPLATE.md`) before scaling sales.
4. Log Domain 1 decision for incentive scheme adoption.
5. Any one-off deal → `INCENTIVE_EXCEPTION_LOG.md` with rationale.
6. Free-core integrity work (red-team, docs, seals) must be a **positive** evaluation factor.

## Procedure — alignment test for a proposed plan
1. Ask: does this pay more if free core is closed or paywalled? If yes → reject.
2. Ask: does this hide ownership/influence (Domain 2)? If yes → reject.
3. Document in decision log.

## Commands
```bash
cat docs/specs/artefacts/06/COMPENSATION_PHILOSOPHY.md
ls docs/specs/artefacts/06/
```

## Done when
- [x] Philosophy public
- [ ] Bands published at first hire
- [ ] Exception log used if any special deal
