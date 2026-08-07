# Checkpointing and intermediate release

**Status:** DEFERRED  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Intermediate checkpoints are part of TTLLM bone. Define schedule, format, storage, and public index.

## Why (ethos)

Final weights only hide the path; paths are the science.

## Prerequisites

- Object storage (R2 or other)
- Training stack

## What to do (executable instructions)

1. Define checkpoint interval (steps/tokens) and retention policy public before run.
2. Store sha256 per shard; seal manifests.
3. Publish at least a subset of intermediates if full dump is cost-prohibitive — with honest statement of what is missing.
4. Document how to resume from public checkpoint.
5. Budget storage separately from FLOPs.

## Artefacts to produce

- Checkpoint policy MD
- Manifests
- Resume guide

## Already done in this vault/repo

- Policy intent in architecture docs

## Deferred / external execution

- Multi-TB public hosting bill

## Risks and soft-tissue anti-patterns

- Secret intermediates
- Undocumented gaps

## Related branches

- 03-technology/06-cryptographic-provenance.md
- 08-ops/07-r2-storage.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
