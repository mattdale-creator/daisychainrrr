# ttlink engine (production)

**Status:** DEFERRED  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Production-scale indexing and query path for human-viewable provenance across training corpora.

## Why (ethos)

Reference demos without production path leave the product unproven at scale.

## Prerequisites

- Corpus
- Infra budget
- SRE

## What to do (executable instructions)

1. Benchmark index classes on target corpus size (latency, memory, recall).
2. Design public free tier query limits vs paid tier.
3. Implement binding of hits to Merkle leaves.
4. Load test; publish SLOs honestly.
5. Open-source the engine or enough to reproduce index on free-core data.
6. Plan abuse: scraping, prompt injection into index UI, legal takedown.

## Artefacts to produce

- Benchmark report
- SLO doc
- Engine repo or modules
- Runbooks

## Already done in this vault/repo

- free_core/ttlink reference

## Deferred / external execution

- Full production deployment

## Risks and soft-tissue anti-patterns

- Fake low latency on tiny corpus only
- Closed index with open weights

## Related branches

- 02-product/03-ttlink.md
- 09-epochs/EPOCH-03-ttlink-production.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
