# Canary + QueryGuard public policy card

**Updated:** 2026-08-08  
**Code:** `free_core/security/canary.py`, `free_core/security/query_guard.py`  
**Ethos:** Throttle abuse without destroying transparency. Never paywall verification.

## Canary documents

| Item | Value |
|------|--------|
| Purpose | Detect ttlink index poisoning / silent doc removal |
| Prefix | `TTLLM_CANARY_UNIQUE_` |
| Default secret (reference) | `bone-not-soft-tissue` |
| Nano public canary id | `ttllm-public-canary-v1` (where injected by pipeline) |
| Presence check | `python3 -m free_core.ttlink.cli canary-check --index <index.json>` |
| Training rule | Canary text **must not** appear in training data |

### Operator duties
1. Inject canary into every public ttlink index before seal.
2. On `check_canary` fail against a claimed-green index → Domain 5 High integrity path.
3. Rotate secret only with public note + re-seal (do not silent-rotate).

## QueryGuard (rate / abuse)

Default constructor parameters (`QueryGuard`):

| Parameter | Default | Meaning |
|-----------|---------|---------|
| `window_sec` | 60.0 | Sliding window seconds |
| `hard_limit` | 120 | Max requests per client per window |
| `suspicious_limit` | 30 | Stricter cap once client marked suspicious |

Behaviour:
- At/over `hard_limit` → deny + mark suspicious
- Suspicious clients limited to `suspicious_limit` in window
- Does **not** encrypt or hide public corpus; only throttles bulk extract

### Public research access
- Local offline verify/query of published indexes: **unlimited** (no QueryGuard) — download artefacts, run CLI.
- Hosted demo API (when live): subject to defaults above.
- Higher hosted quota: email **md@0265.au** with research purpose; grants are discretionary, logged if material (Domain 1), never require waiving free-core rights.

### What QueryGuard is not
- Not a substitute for BOUNDARY
- Not a paywall on manifests
- Not a content filter for political speech
- Not a claim of DDoS-proof production (Cloudflare edge is separate)

## Related
- Domain 10 red-team harness: `scripts/redteam_nano_harness.py`
- Handbook: `docs/handbook/domains/10-redteam-ops.md`
