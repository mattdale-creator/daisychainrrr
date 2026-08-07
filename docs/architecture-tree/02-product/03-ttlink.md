# ttlink — human-viewable provenance links

**Status:** PARTIAL  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

System linking model outputs (and decisions) to training sources, checkpoints, and traces in forms non-specialists can follow. Product is the proof when links work.

## Why (ethos)

Without ttlink, transparency is not usable by the public.

## Prerequisites

- Tokenised corpus or demo corpus
- Index technology
- UI/API

## What to do (executable instructions)

1. Specify span → hits API: offsets, context windows, document identifiers, sha256 of docs.
2. Bind index leaves to Merkle manifests (cryptographic provenance branch).
3. Ship and test reference implementation for small corpora (free_core/ttlink).
4. Plan production class index (suffix array / FM-index / infini-gram class) for Epoch 03.
5. Enterprise tier may add retention/SSO/SLA but must not gate basic public linking for free-core models.
6. Publish honest accuracy: exact match vs approximate; never imply exact when approximate.

## Artefacts to produce

- OpenAPI for ttlink
- Binding manifest schema
- Reference UI
- Eval set for link quality

## Already done in this vault/repo

- free_core/ttlink reference
- docs/architecture/ttlink.md

## Deferred / external execution

- Multi-trillion-token production index

## Risks and soft-tissue anti-patterns

- 'Inspired by' without honesty
- Paywalling basic links

## Related branches

- 03-technology/05-ttlink-engine-production.md
- 02-product/04-free-public-core.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
