# Public stream (real data)

**Status:** PARTIAL  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Publicly readable stream of real training/eval/ops events (not marketing fake ticks). Reference implementation in free_core/stream; production scale is Epoch 03.

## Why (ethos)

Transparency you cannot watch in motion is incomplete.

## Prerequisites

- Event schema
- Storage (R2/object or log backend)
- Abuse controls plan

## What to do (executable instructions)

1. Define event types: checkpoint sealed, eval run, red-team finding summary, release, tombstone.
2. Implement append-only public feed with content hashes.
3. Ship reference stream module and sample events (done at scaffold).
4. Rate-limit and redact secrets; never stream private keys or PII.
5. Expose stream URL on site when non-empty; until then document deferred honestly.
6. Bind stream entries into Merkle/manifest chain when provenance stack is live.

## Artefacts to produce

- Event schema JSON
- Public stream endpoint
- Sample events
- Abuse policy

## Already done in this vault/repo

- free_core/stream scaffold
- docs/architecture notes

## Deferred / external execution

- Always-on production stream at training scale

## Risks and soft-tissue anti-patterns

- Fake heartbeat events
- Streaming secrets

## Related branches

- 03-technology/07-public-stream-infra.md
- 03-technology/06-cryptographic-provenance.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
