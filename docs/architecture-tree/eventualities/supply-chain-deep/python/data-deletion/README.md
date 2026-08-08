# Supply chain · python · data-deletion

**Path:** `eventualities/supply-chain-deep/python/data-deletion/README.md`  
**Updated:** 2026-08-08  
**Domain:** 7 (Supply-Chain and Dependency Transparency)

## What this eventuality is
Material dependency **python** experiences: **upstream or local data was deleted**.

## Dependency register
See `registers/supply-chain/DEPENDENCY_REGISTER.md`.  
python is listed as part of public core hosting, training, data, or tooling.

## Detection signals
1. Provider status page / API errors / failed deploys / failed data fetches.
2. License or ToS notice email; pricing change notice.
3. Verify scripts fail (e.g. PG fetch, Cloudflare deploy, GitHub push, torch import).
4. Account login anomalies (possible takeover).

## Immediate response
1. Confirm blast radius: which free-core surfaces break (site, seals, training, ttlink, stream)?
2. Log in Domain 5 incident log if public proof surfaces degraded; Domain 7 change log for dependency substitution.
3. Fail closed on public claims if verification path is broken.
4. Prefer alternate public path (mirror, cold archive, secondary remote) without closing free core.
5. If data/source license changes, Domain 3 legal process — no silent corpus rewrite.
6. Stream event `supply_chain` with provider + impact summary (no secrets).

## Prevention
- Dependency register kept current on material changes.
- Prefer open tools and public-domain data where possible.
- Secrets never in git; token least-privilege (ops/HUMAN_GATES.md for scope gaps).
- Document failover for site (Pages) and for model artefact hosting.

## Tests / drills
- [ ] Simulate deploy failure; confirm incident template works
- [ ] `prepare_data` failure path documented with tombstone option
- [ ] Annual Domain 7 attestation lists this provider

## Owner
Project lead + whoever holds the python account.  
Security-sensitive: treat account-takeover as Critical under Domain 5 thresholds.

## Related
- `docs/specs/07-supply-chain.md`
- `registers/supply-chain/`
