# Source of truth (SoT) rules

**Status:** DONE  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Single Mac vault `TTLLMS.com BUILD` is the operational source of truth for paths, secrets location, DNS bind files, precompact snapshots, and architecture tree. Public code lives in GitHub `mattdale-creator/daisychainrrr`. Secrets never enter git.

## Why (ethos)

Without a single SoT, agents and humans fork reality; soft tissue proliferates.

## Prerequisites

- Vault path exists
- Repo symlink or clone under `01-repo/daisychainrrr`

## What to do (executable instructions)

1. Treat `/Users/hattr/Downloads/TTLLMS.com BUILD` as SoT for ops artefacts (DNS txt, secrets.local.env path, freezes).
2. Treat GitHub main as SoT for public free-core code and published docs (after push).
3. Mirror architecture-tree vault → `docs/architecture-tree/` before any public claim of architect complete.
4. Never commit `ops/secrets.local.env` or tokens; keep gitignore enforced.
5. If vault and repo disagree, vault wins for paths/ops; repo wins for already-pushed public code until deliberately re-synced.
6. Record SoT path in `SOURCE_OF_TRUTH_PATH.txt` at repo root for agents.

## Artefacts to produce

- SOURCE_OF_TRUTH_PATH.txt
- Vault README
- Mirrored architecture-tree

## Already done in this vault/repo

- Vault layout
- Repo clone/symlink
- Precompact skill path freeze

## Deferred / external execution

- Multi-machine replication policy (epoch 05)

## Risks and soft-tissue anti-patterns

- Second secret SoT in chat history
- Pushing secrets
- Editing live site without vault site copy

## Related branches

- 08-ops/01-vault-layout.md
- 08-ops/04-secrets-and-tokens.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
