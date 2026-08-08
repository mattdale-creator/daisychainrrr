# Commercial isolation

**Updated:** 2026-08-08  
**Owner (R):** Boundary Custodian + commercial product owner  
**Canonical:** `commercial/ISOLATION_RUNBOOK.md`  
**BOUNDARY:** `commercial/BOUNDARY.md`  
**Domain ops:** `docs/handbook/domains/08-boundary-ops.md`

## Purpose
Monetise **outside** the free public core without contaminating the skeleton. Customer compromise must not alter public proof; public compromise must not leak tenant data.

## Hard rules
1. Separate infrastructure identity, databases, and **signing keys** from public core.
2. Same provenance philosophy *inside* customer boundary — without publishing private weights/data.
3. Red-team commercial surface with equal intensity to public transparency layer.
4. No commercial feature may require closing public TTLLM / basic ttlink / manifests.
5. Free public core and BOUNDARY take precedence over revenue.

## Isolation checklist (before paid feature ships)
- [ ] BOUNDARY updated if needed (Domain 8) + Domain 1 decision
- [ ] Tenant isolation design reviewed (accounts, storage, logs, keys)
- [ ] Signing keys **not** shared with public release keys
- [ ] Contracts lack core-closure clauses (Domain 2: no side letters)
- [ ] Customer prompts/docs never enter public train mix without explicit licensed publication path
- [ ] Scorecard row: commercial impact on free core = **none**
- [ ] Public status does not depend on paid API for verification
- [ ] Incident playbook knows who can touch public vs tenant systems

## Architecture sketch (founding)
```
[Public free core]          [Commercial arm]
  GitHub public               Private tenant envs
  FREE_CORE_SEAL              Customer data stores
  nano weights/ttlink         Hosted SLA / VPC options
  public stream               Private ops metrics
  demo/public keys            Distinct signing keys
         \                     /
          \— BOUNDARY wall —/
```

## Procedure — review a design for isolation
1. Draw data flows: what crosses wall?
2. For each flow: allowed under BOUNDARY?
3. Can a public verify still work offline with published artefacts only?
4. If customer fine-tune: is lineage to public core published without leaking private data?
5. Document residual risks in SKU one-pager under `commercial/skus/`.

## Failure modes
| Failure | Response |
|---------|----------|
| Tenant data in public seal path | Critical incident; scrub; Domain 3 process |
| Public claim requires paid login | BOUNDARY violation — refuse / remove |
| Shared signing key | Rotate; treat as key-compromise class |
| Side letter closes core | Reject contract; Domain 1 + 2 |

## Commands (public side still must pass)
```bash
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
python3 scripts/redteam_nano_harness.py
cat commercial/BOUNDARY.md
cat commercial/ISOLATION_RUNBOOK.md
```

## RACI
Boundary Custodian R for wall integrity; commercial owners R for tenant design; project lead A; public I via BOUNDARY publication.

## Done when
- [ ] Checklist complete for the feature
- [ ] SKU one-pager updated
- [ ] No open BOUNDARY conflicts
