# Cryptographic provenance (SHA-256, Merkle, Ed25519)

**Status:** PARTIAL  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Seal artefacts with hashes, Merkle trees, and signatures so third parties can verify integrity without trusting marketing pages.

## Why (ethos)

Unverifiable transparency is soft tissue.

## Prerequisites

- free_core/provenance tooling
- Key ceremony plan

## What to do (executable instructions)

1. Hash every released artefact (sha256).
2. Build Merkle manifests for release sets; publish roots.
3. Sign roots with Ed25519 (or stronger); publish public keys with rotation policy.
4. Store keys offline/HSM when org matures; for now document threat model for key leakage.
5. Integrate with stream events and ttlink leaves.
6. Provide verify CLI in free_core.

## Artefacts to produce

- Manifest schema
- Verify CLI
- Public keys
- Rotation policy

## Already done in this vault/repo

- free_core/provenance scaffold
- schemas

## Deferred / external execution

- HSM-backed org keys
- Timestamping authority integration

## Risks and soft-tissue anti-patterns

- Unsigned 'trust us' releases
- Keys in git

## Related branches

- 04-security/05-index-and-provenance-integrity.md
- 02-product/02-public-stream.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
