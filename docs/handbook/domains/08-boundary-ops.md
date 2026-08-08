# Domain 8 — Boundary operations (human handbook)

**Updated:** 2026-08-08  
**Owner (R):** Boundary Custodian (project lead until staffed)  
**Normative:** `docs/specs/08-boundary-rules.md`  
**Canonical BOUNDARY:** `commercial/BOUNDARY.md`  
**Isolation:** `commercial/ISOLATION_RUNBOOK.md`  
**Refuse script:** `docs/handbook/commercial/02-refuse-close-core.md`  
**SKU go-live:** `docs/handbook/commercial/03-sku-go-live.md`

## Purpose
Hard line: free public core stays free; commercial privacy only in allowed categories.

## Precedence rule (public)
**Free public core and BOUNDARY take precedence over commercial convenience and revenue.**

## Procedure — review a proposed commercial feature

1. Read `commercial/BOUNDARY.md` (Allowed vs Prohibited lists).
2. Checklist:
   - [ ] Does it require paywalling verification of a public-core claim? → **Reject**
   - [ ] Does it sell exclusive free-core weights/data/basic ttlink? → **Reject**
   - [ ] Does it need silent alteration of public artefacts? → **Reject**
   - [ ] Is privacy limited to customer data / service ops / allowed list? → Continue
3. If accept: Domain 1 decision; update SKU one-pager under `commercial/skus/`.
4. Isolation review: `docs/handbook/commercial/01-isolation.md`.
5. Contracts: no side letters (Domain 2); no close-core clauses.
6. Launch only via SKU go-live handbook.

## Procedure — change BOUNDARY itself

1. Material Domain 1 decision **before** implementation.
2. Update `commercial/BOUNDARY.md` + `docs/specs/artefacts/08/*`.
3. Public note / scorecard.
4. Re-train sellers/partners.

## Commands
```bash
cat commercial/BOUNDARY.md
cat commercial/ISOLATION_RUNBOOK.md
ls commercial/skus/
```

## RACI
Boundary Custodian R; commercial product owners must surface pressure early; public-core leads may challenge.

## Done when
- [x] BOUNDARY published
- [x] Isolation runbook published
- [ ] First SKU live under this process (none sold yet)
