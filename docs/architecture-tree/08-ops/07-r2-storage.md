# R2 storage

**Status:** DEFERRED  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Cloudflare R2 for checkpoints, corpora samples, stream archive. Requires dashboard enable (API error 10042 until enabled).

## Why (ethos)

Public bone needs durable object storage.

## Prerequisites

- Cloudflare account
- Billing if required
- Dashboard enable R2

## What to do (executable instructions)

1. Enable R2 in Cloudflare dashboard.
2. Create buckets: e.g. ttllms-public, ttllms-private (private never for free-core bone that should be public).
3. Issue S3-compatible keys to secrets.local.env.
4. Document public vs private bucket policy aligned with BOUNDARY.
5. Estimate costs for checkpoint plans before training.
6. Versioning and lifecycle rules for intermediates.

## Artefacts to produce

- Buckets
- Keys in env
- Policy MD
- Cost estimate

## Already done in this vault/repo

- R2 keys prepared in past session context; enable still human gate

## Deferred / external execution

- Dashboard enable + first public object

## Risks and soft-tissue anti-patterns

- Putting free-core weights only in private bucket
- Keys in git

## Related branches

- 03-technology/03-checkpointing.md
- 08-ops/04-secrets-and-tokens.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
