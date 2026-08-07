# Precompact path preserve

**Status:** DONE  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Skill + hooks freeze conversation path and inject after compact so TTLLMS vault goals survive context loss. Not full invisible history restore — path + freeze pack.

## Why (ethos)

Compaction without freeze loses the build.

## Prerequisites

- Skill installed under ~/.grok/skills/precompact-path-preserve

## What to do (executable instructions)

1. Keep PreCompact/PostCompact hooks enabled.
2. On freeze: write PRECOMPACT_CONVERSATION.md, POST_COMPACT_INJECT.md, chat_history.jsonl under freeze id.
3. Vault copies under 09-precompact-snapshots; Desktop archive per user preference.
4. After compact: read inject first, then continue architect/execution from STATUS.
5. Do not enable dormant new-session handoff unless user asks (default OFF).
6. Trigger manually with /precompact-path-preserve when needed.

## Artefacts to produce

- Freeze packs
- Inject files
- Hook config

## Already done in this vault/repo

- Skill installed
- Hooks
- Freezes performed this project

## Deferred / external execution

- Seamless full invisible multi-session memory (product limit)

## Risks and soft-tissue anti-patterns

- Assuming freeze = full CoT restore
- Auto-spawning sessions without consent

## Related branches

- 08-ops/10-new-session-handoff-dormant.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
