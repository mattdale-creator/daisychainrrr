# Index and provenance integrity

**Status:** HOWTO  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Defend ttlink index and manifests against poisoning, rollback, and domain hijack.

## Why (ethos)

Forged provenance is worse than no provenance.

## Prerequisites

- Crypto provenance stack
- DNS/account security

## What to do (executable instructions)

1. Sign manifests; monitor root transparency.
2. Protect Cloudflare/GitHub accounts with hardware keys when possible.
3. Detect index poisoning via canary documents.
4. Incident playbook for key compromise and domain loss.
5. Third-party mirrors of roots encouraged in Epoch 05.

## Artefacts to produce

- Canary design
- Incident playbook
- Account hardening checklist

## Already done in this vault/repo

- Provenance scaffold

## Deferred / external execution

- External auditors
- Multi-sig releases

## Risks and soft-tissue anti-patterns

- Single laptop root of trust forever
- No canaries

## Related branches

- 03-technology/06-cryptographic-provenance.md
- 08-ops/02-cloudflare-account.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
