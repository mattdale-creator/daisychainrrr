# Training stack for a TTLLM release

**Status:** DEFERRED  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Open training code + configs + logs + hardware disclosure. Founding order-of-magnitude: 32B-class full project ~$4–8M; 7–13B substantially less. Verify with current quotes.

## Why (ethos)

Without open training code and configs, reproducibility dies.

## Prerequisites

- Budget
- Cluster or cloud credits
- Data plan
- License strategy

## What to do (executable instructions)

1. Choose first public release scale (recommend 7B–13B learning run before 32B).
2. Publish training code under free-core license from day one of serious runs.
3. Version every hyperparameter and seed; store configs in git tags matching checkpoints.
4. Record hardware SKU, region, provider in supply-chain doc (Domain 7).
5. Budget with founding OOM then replace with real quotes; keep cost ledger public where possible.
6. Treat ablations with same release discipline as final run (smaller scale OK).
7. Refuse 'we will open later' without dated public commitment.

## Artefacts to produce

- Training repo
- Config versions
- Run cards
- Cost ledger
- Hardware disclosure

## Already done in this vault/repo

- Cost narrative in docs/business
- Architecture free-core intent

## Deferred / external execution

- Actual training runs and payment

## Risks and soft-tissue anti-patterns

- Secret training code + public weights only
- Unlogged seeds

## Related branches

- 03-technology/03-checkpointing.md
- 05-business/01-unit-economics-math-physics.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
