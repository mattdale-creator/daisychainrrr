# Founding Provenance Binding

**Schema:** ttllm.founding_provenance.v1  
**Sealed:** 2026-08-07T18:11:08Z  
**Repository:** mattdale-creator/daisychainrrr

## Layer A — Account export

| Field | Value |
|-------|-------|
| conversation_id | `8a75e0b4-1a78-4926-a7e5-7227e9ff3b33` |
| title | Totally Transparent LLMs: OLMo and LLM360 |
| create_time | 2026-08-07T15:48:49.121530Z |
| modify_time | 2026-08-07T17:06:17.539Z |
| model | grok-4-heavy |
| source | iOS |
| export zip | `a0e32d9f-e1ef-41f8-b167-b39cdf58487f.zip` |
| TRANSCRIPT_ONLY.md sha256 | `76d57d5a2c9778f322b6779b4783f3dfc5238907f4d4aece2ff0f45309e02f2e` |

## Layer B — Device capture (Proof RIP)

| Field | Value |
|-------|-------|
| files | IMG_3305–IMG_3359 (55 PNGs) |
| EXIF | 2026-08-08 00:04:33–01:13:19 Australia/Perth |
| creator | com.apple.springboard |
| quarantine | sharingd @ 2026-08-07 17:13:29 UTC |

## Layer C — Repo seal

`make seal` → `manifests/FREE_CORE_SEAL.json`

## Verification

1. Read `founding/conversation/TRANSCRIPT_ONLY.md`  
2. Verify Proof RIP hashes if PNGs present  
3. `ttllm-manifest verify --manifest manifests/FREE_CORE_SEAL.json --base .`
