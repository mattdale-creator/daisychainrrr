# Threat model — TTLLM free public core + transparency systems

**Updated:** 2026-08-08  
**Scope:** Public free core, site, seals, ttlink, stream, BOUNDARY.  
**Not in scope as “solved”:** full frontier model safety (capital/scale).

## Assets
| Asset | Criticality |
|-------|-------------|
| FREE_CORE_SEAL / release manifests | Critical |
| Public stream chain tips | High |
| ttlink indexes + canaries | High |
| Demo vs production signing keys | Critical if confused |
| Domains ttllms.com / .org | High |
| BOUNDARY + decision log honesty | High |
| Customer tenant data (future commercial) | Critical (isolation) |

## Adversaries
1. **Opportunistic vandal** — deface site, break vanity metrics  
2. **Integrity attacker** — forge green seals, poison index, break stream silently  
3. **Commercial capture** — pressure to paywall verify or close core  
4. **Insider** — single-human key/DNS abuse (concentration risk public)  
5. **Supply-chain** — malicious dependency in free_core path  

## Threat → mitigation map
| Threat | Impact | Mitigation (current) | Residual |
|--------|--------|----------------------|----------|
| Manifest forgery | False trust | Merkle verify CLI; tamper tests in harness | Demo keys not prod (T5) |
| Seal staleness after edit | False green | `check_seal_freshness.py` + oneshot | CI workflow push blocked (T4) |
| Stream backdate | Fake history | Hash chain verify | Need social process for tip publish |
| Index poison | Wrong provenance spans | Canaries + check | Production multi-TB not built |
| Bulk extract abuse | Hosted cost | QueryGuard | Local offline unlimited by design |
| DNS hijack | Site spoof | CF account 2FA (human); registrar | Org DNS open (T1) |
| Close-core contract | Ethos death | BOUNDARY + refuse handbook + placeholders | Revenue pressure future |
| Key confusion | Fake “HSM” trust | Explicit demo≠prod language | T5 ceremony pending |
| Tenant→public leak | Privacy + integrity | Isolation runbook | No paid tenants yet |

## Remember you are on drugs (founding)
Measure. Multi-AI battery. Red-team. Prefer artefacts over narrative. This model is re-read before any “complete” claim.

## Related
- `scripts/redteam_nano_harness.py`  
- `docs/handbook/incident/*`  
- `docs/placeholders/security/*`  
- Architecture HOWTO: `docs/architecture-tree/04-security/01-threat-model.md`
