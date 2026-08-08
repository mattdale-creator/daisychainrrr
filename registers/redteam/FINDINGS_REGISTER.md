# Public Red-Team Findings Register

**Normative:** Domain 10 · `docs/specs/artefacts/10/`  
**Campaign JSON:** `registers/redteam/campaign_RTC-2026-08-08.json`  
**Harness:** `scripts/redteam_nano_harness.py` · `scripts/redteam_campaign_2026_08_08.py`

| ID | Discovered | Published | Component | Severity | Summary | Remediation | Residual |
|----|------------|-----------|-----------|----------|---------|-------------|----------|
| RT-C-001 | 2026-08-08 | 2026-08-08 | free_core_seal / status | High | FREE_CORE_SEAL can go stale while file verify still true; status API correctly reports `fresh: false` when new files added (campaign script). Misread as “green” if only `verify_ok` checked. | Document: green = verify **and** fresh. oneshot + `ttllm_status --quiet-ok` require both. Campaign run reseals after. | Operators must not treat verify-only as green. |
| RT-C-002 | 2026-08-08 | 2026-08-08 | keys | Medium | `examples/keys/demo.private.pem` was included in FREE_CORE_SEAL leaves (tutorial private key content-addressed in free-core seal). | **Fixed:** seal_targets excludes `*.private.pem` / private key patterns. README already forbids prod-root language. | Tutorial private key remains in git for demos; not in Merkle free-core seal after fix. Never use as production root (T5). |
| RT-C-003 | 2026-08-08 | 2026-08-08 | nano_release | High (prior loop) | nano-v2 RELEASE_MANIFEST failed after `cost_ledger.md` regen without reseal. | **Fixed prior loop:** reseal nanos; cost_ledger script warns to reseal. | Regen cost_ledger requires reseal. |
| RT-C-004 | 2026-08-08 | 2026-08-08 | site / dns | Low / gate | ttllms.org does not resolve (T1). | Not a software defect; hard gate. | Tombstone on URL inventory. |
| RT-C-005 | 2026-08-08 | 2026-08-08 | process | Medium | Standing red-team hire absent (T10); automated harness ≠ human campaign depth. | Cadence in TESTING_LOOP.md; this campaign expands automated surface. | Hire remains T10. |
| RT-C-006 | 2026-08-08 | 2026-08-08 | site/api | Medium | Live Pages `POST /api/ttlink/` is unauthenticated; no QueryGuard on edge Function. | **Partial fix (post-loop continue):** best-effort per-isolate QueryGuard on `functions/api/ttlink.js` (hard_limit 60 / unique_span_burst 40); GET exposes `query_guard` stats; honesty: not multi-POP Durable Object production guard. Offline CLI unlimited. | Residual: isolate-local only; multi-TB production still needs DO/gateway rate limit (scale path, not faked). |
| BH-001…012 | 2026-08-08 | 2026-08-08 | business/boundary | — | Black-hat business campaign BHA-2026-08-08: 14/14 automated probes pass after detector precision fix. | Real code: `free_core/business/boundary_guard.py`, `scripts/redteam_business_attack.py` | Free-rider + T8/T9/T11 remain business residual (by design or hard gate). |

## Campaign RTC-2026-08-08 automated probes (20)

| Probe | Sev | Result |
|-------|-----|--------|
| RT-001 manifest leaf tamper | Critical | PASS |
| RT-002 merkle root lie | Critical | PASS |
| RT-003 stream payload tamper | Critical | PASS |
| RT-004 stream prev_hash splice | Critical | PASS |
| RT-005 canary present/absent | High | PASS |
| RT-006 QueryGuard hard limit | Medium | PASS |
| RT-007 QueryGuard span burst | Medium | PASS |
| RT-008 FREE_CORE_SEAL verify | Critical | PASS |
| RT-009 inclusion proof | High | PASS |
| RT-010 all nano RELEASE_MANIFEST | High | PASS |
| RT-011 status nanos + seal fresh | High | FAIL then fixed (stale after campaign file; reseal) |
| RT-012 BOUNDARY paywall forbid | High | PASS |
| RT-013 claim gate frontier | Medium | PASS |
| RT-014 demo private in seal | Medium | Noted → fixed exclude |
| RT-015 nano stream events | Medium | PASS |
| RT-016 hard gates open honesty | High | PASS |
| RT-017 status_snapshot ethos | Medium | PASS |
| RT-018 secrets.local.env not sealed | Critical | PASS |
| RT-019 offline CLI unlimited | Low | PASS |
| RT-020 disk hash binds leaf | Low | PASS |

## Default
Publish. No permanent suppression.
