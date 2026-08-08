# SKU go-live

**Updated:** 2026-08-08  
**Owner (R):** Commercial product owner  
**Boundary gate:** Boundary Custodian  
**SKU one-pagers:** `commercial/skus/`  
**Status:** All founding SKUs **designed / not sold**

## Purpose
Ship paid offerings only when isolation + BOUNDARY + disclosure are honest. Go-live is a process, not a Stripe toggle.

## Designed SKUs (founding)
| SKU file | Intent |
|----------|--------|
| `hosted-infra.md` | Hosted reliability / compliance around inspectable models |
| `enterprise-ttlink.md` | Enterprise audit tooling (not exclusive public basic ttlink) |
| `certified-finetunes.md` | Fine-tunes with published lineage constraints |
| `analysis-workbench.md` | Analysis tools that do not gate core verification |
| `priority-support.md` | Human support SLA |
| `taas-methodology.md` | Methodology / TaaS licensing |

## Go-live checklist (every SKU)

### A. Ethos / legal
- [ ] Read `commercial/BOUNDARY.md` — no prohibited opacity
- [ ] Isolation checklist complete ([01-isolation](01-isolation.md))
- [ ] Domain 1 decision logged (launch is material when first revenue or public commercial claim)
- [ ] Contracts: no core-closure clauses; no side letters (Domain 2)
- [ ] Domain 3: customer data path cannot launder into silent public claims
- [ ] Pricing may be private; **capability claims used publicly** must match free-core eval honesty

### B. Technical
- [ ] Distinct infra identity and keys from public release signing
- [ ] Public verify path still works offline / unpaid
- [ ] Monitoring: tenant compromise ≠ public seal rewrite
- [ ] Red-team pass on commercial surface (Domain 10 scope expansion)

### C. Public honesty
- [ ] SKU one-pager status → `live` with date only when truly selling
- [ ] Scorecard notes commercial launch; free-core impact = none
- [ ] Site commercial copy matches BOUNDARY (no "exclusive bone")
- [ ] Annual boundary attestation plan once selling (Domain 8)

### D. Operations
- [ ] Support contact + escalation
- [ ] Incident: which playbook for tenant vs public
- [ ] Billing / entity existence (human gate — no fake company)

## Procedure
1. Draft or update `commercial/skus/<sku>.md`.
2. Boundary review meeting notes → decision log if material.
3. Isolation design review sign-off.
4. Implement technical + legal packaging.
5. Soft launch: limited customers, high observation.
6. Flip status to live; update STATUS_HONEST if org claim changes.
7. Schedule first boundary attestation date.

## Refuse path
If any checklist item forces close-core → [02-refuse-close-core](02-refuse-close-core.md).

## Commands
```bash
ls commercial/skus/
cat commercial/BOUNDARY.md
cat commercial/ISOLATION_RUNBOOK.md
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
```

## RACI
Commercial owner R for delivery; Boundary Custodian R for wall; project lead A; Domain 2/3 C; public I via BOUNDARY + status.

## Done when
- [ ] Checklist complete
- [ ] First invoice or signed SOW only after checklist
- [ ] Public docs not lying about free core
