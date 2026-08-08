# Domain 2 — Ownership, funding, influence (human handbook)

**Updated:** 2026-08-08  
**Owner (R/A):** project lead (md@0265.au)  
**Normative:** `docs/specs/02-ownership-funding.md`  
**Artefacts:** `docs/specs/artefacts/02/`  
**Register:** `registers/ownership/`

## Purpose
Disclose who owns and funds the project so capture risk is visible.

## Current bootstrap state (update when it changes)
- Cap table: 100% project lead — `docs/specs/artefacts/02/CAP_TABLE_SUMMARY.md`
- Funding: $0 institutional — `FUNDING_HISTORY_LOG.md`
- Influence rights: **none** — `INFLUENCE_RIGHTS_REGISTER.md`
- Side letters: **prohibited** — `SIDE_LETTER_PROHIBITION.md`

## Procedure — material ownership/funding change (≤14 days)

1. Update cap table summary and/or funding history with plain-language control terms.
2. Update influence rights register (explicit “none” if applicable).
3. Log Domain 1 decision (`registers/decisions/LOG.md`).
4. Reject or remove any right that can force free-core opacity (Domain 8).
5. Update master domain scorecard Domain 2 row.
6. Optional annual attestation: use `ANNUAL_ATTESTATION_TEMPLATE.md`.

## Procedure — refuse bad capital terms

1. Read `commercial/BOUNDARY.md` and Domain 8 handbook.
2. If term requires closing free core or secret side letter → **refuse**.
3. Log decision D-NNNN with options and rationale.
4. Do not sign; update influence register if anything was signed historically.

## Commands
```bash
ls docs/specs/artefacts/02/
ls registers/ownership/
cat docs/specs/artefacts/02/INFLUENCE_RIGHTS_REGISTER.md
```

## RACI
Project lead: R+A until entity board exists. Future board: A for influence disclosures.

## Done when
- [x] Current disclosures published
- [ ] 14-day update rule exercised on first real financing
- [ ] Annual attestation once entity exists
