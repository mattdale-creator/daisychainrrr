# Domain 1 — Monthly governance audit

**Period:** 2026-08-01 → 2026-08-08 (bootstrap partial month)  
**Auditor:** project lead / agent pair (founding)  
**Date filed:** 2026-08-08  
**Status:** PARTIAL — first ritual execution; not yet a full 30-day independent review

## Scope checked
- [x] `registers/decisions/LOG.md` present and append-only format
- [x] `registers/decisions/feed.json` machine feed exists
- [x] Material decisions D-0001–D-0022 logged (handbook, seals, nanos, leaves)
- [x] No permanent secret exceptions without expiry found in decision log
- [x] BOUNDARY still public at `commercial/BOUNDARY.md`
- [x] FREE_CORE_SEAL path known (`manifests/FREE_CORE_SEAL.json`)
- [ ] Full git history review of every commit vs decision materiality (deferred — volume; next month)
- [ ] Independent second auditor (no second human yet — tombstone)

## Gaps / backfills
| Gap | Action |
|-----|--------|
| D-0019 / D-0020 IDs skipped | Accept numbering hole; next id D-0023 |
| Monthly audit never run before | This file is first |
| Quarterly report not full period | Bootstrap report exists under artefacts |

## Verification commands run
```bash
python3 scripts/oneshot_verify_all.py
python3 scripts/redteam_nano_harness.py
python3 scripts/check_data_cards.py
# after this audit wave also:
# python3 scripts/check_seal_freshness.py
# python3 scripts/public_verify_harness.py
```

## Score (Domain 1)
**PARTIAL** — log path used; ritual started; full monthly independence and complete commit sweep not MET.

## Next actions
1. Next audit on/after 2026-09-08 with full 30-day commit sweep
2. Keep material decisions ≤7 days
3. Wire CI seal freshness so green status cannot drift silently

## Sign-off
Founding operational audit — not a legal certification.
