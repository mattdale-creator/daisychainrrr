# Threat model

**Status:** HOWTO  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Structured threats: model misuse, supply chain, provenance forgery, insider soft tissue, commercial arm compromise, DDoS on public index, legal coercion.

## Why (ethos)

Unexamined threats become soft tissue surprises.

## Prerequisites

- Security owner (even if founder)

## What to do (executable instructions)

1. Maintain docs/security/threat-model.md and this HOWTO in sync.
2. For each asset (keys, weights, index, stream, domain DNS), list threats and mitigations.
3. Review on each major release.
4. Link red-team findings back into model updates.
5. Separate free-core abuse from enterprise tenant isolation threats.

## Artefacts to produce

- Threat model MD
- Asset inventory for security

## Already done in this vault/repo

- docs/security/threat-model.md scaffold

## Deferred / external execution

- Formal third-party threat model workshop

## Risks and soft-tissue anti-patterns

- Security by obscurity
- Ignoring insider threat

## Related branches

- 04-security/02-frontier-red-team.md
- 04-security/05-index-and-provenance-integrity.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
