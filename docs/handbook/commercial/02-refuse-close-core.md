# Refuse a close-core commercial ask

**Updated:** 2026-08-08  
**Owner (R):** Boundary Custodian (project lead until staffed)  
**BOUNDARY:** `commercial/BOUNDARY.md`  
**Domain:** 8 — Boundary

## Purpose
Script the hard no. Revenue pressure is expected; closing the free public core is not a negotiable trade.

## Precedence (public, non-negotiable)
**Free public core and BOUNDARY take precedence over commercial convenience and revenue.**

## What "close-core" looks like
| Ask | Verdict |
|-----|---------|
| Paywall to download public weights / basic ttlink | **Refuse** |
| Paywall to verify a public claim / get manifests | **Refuse** |
| "Exclusive" public data mix for paying customers only | **Refuse** |
| Silent fine-tune marketed as TTLLM without lineage | **Refuse** |
| Investor term: future right to privatise free core | **Refuse** |
| Remove public artefacts to please a customer | **Refuse** (Domain 3 process only for legal necessity, with tombstone) |
| Hosted SLA, VPC, private docs, certified finetunes with lineage | **Allowed** (see SKUs) |
| Priority support / methodology licensing | **Allowed** |

## Procedure — refuse (internal + external)

### 1. Classify the ask
Map to BOUNDARY Allowed vs Prohibited lists. If unclear → treat as prohibited until Domain 1 decides otherwise **in public log**.

### 2. Internal decision
- Boundary Custodian issues **reject** with BOUNDARY citation.
- Material pressure or exception attempt → Domain 1 decision within 7 days (outcome likely still reject).
- Never approve via side channel without log.

### 3. External response template
```
Thanks for the proposal. TTLLM's free public core (weights and checkpoints under
the TTLLM promise, training data docs, training code for public releases, basic
ttlink, cryptographic manifests, public stream, transparency specs) stays free
and public. We cannot accept terms that paywall verification or close that core.

We can discuss commercial options that sit outside the core — for example hosted
infra with SLA, enterprise audit tooling, certified fine-tunes with published
lineage, priority support, or methodology licensing. See:
https://ttllms.com (commercial boundary) and commercial/BOUNDARY.md in the public repo.

Contact: md@0265.au
```

### 4. Record
- Decision log if material (investor, large customer, policy edge).
- If repeated pressure from same channel: note pattern for stewardship (Domain 9).

### 5. Offer constructive redirect
Point to `commercial/skus/*` one-pagers for allowed monetisation.

## Escalation
| Pressure source | Path |
|-----------------|------|
| Sales | Boundary Custodian veto stands |
| Investor | Domain 1 + public BOUNDARY; covenant language |
| Partner contract | Legal Domain 2/3; no side letters |
| Insider "just this once" | Same as external — log and refuse |

## Anti-patterns
- Softening BOUNDARY in a private deck while public doc stays strict
- "Temporary" close with no expiry
- Renaming paywalled verification as "enterprise support"

## RACI
Boundary Custodian R/A for refuse; commercial may Consult; leadership cannot override without public Domain 1 change to BOUNDARY itself (which is its own high bar).

## Done when
- [ ] Ask mapped to BOUNDARY
- [ ] Refuse delivered with alternative if any
- [ ] Material events logged
