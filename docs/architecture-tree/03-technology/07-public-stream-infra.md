# Public stream infrastructure

**Status:** DEFERRED  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Hosting, retention, CDN, and abuse controls for the public event stream.

## Why (ethos)

A stream that dies when a laptop sleeps is not public infrastructure.

## Prerequisites

- Cloud account
- Object/log store
- Domain

## What to do (executable instructions)

1. Choose storage (R2, etc.) and append-only pattern.
2. Serve via Pages/Workers or static+API hybrid.
3. Retention policy public; cold archive plan.
4. Monitor cost; stream is free-core cost center funded by outer layers.
5. Incident: if stream compromised, Domain 5 disclose.

## Artefacts to produce

- Infra diagram
- Cost estimate
- Runbook

## Already done in this vault/repo

- Reference stream code

## Deferred / external execution

- Always-on multi-region stream

## Risks and soft-tissue anti-patterns

- Laptop-only stream presented as production

## Related branches

- 02-product/02-public-stream.md
- 08-ops/07-r2-storage.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
