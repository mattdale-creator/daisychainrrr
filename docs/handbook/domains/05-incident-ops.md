# Domain 5 — Incident operations (human handbook)

**Updated:** 2026-08-08  
**Owner (R):** Incident Response Owner (project lead until staffed)  
**Normative:** `docs/specs/05-incident-disclosure.md`  
**Policy:** `docs/specs/artefacts/05/INCIDENT_DISCLOSURE_POLICY.md`  
**Severity:** `docs/specs/artefacts/05/SEVERITY_THRESHOLDS.md`  
**Register:** `registers/incidents/INCIDENT_LOG.md`  
**Playbook (High/Critical):** `docs/handbook/incident/01-high-critical-playbook.md`

## Severity (summary)

| Level | Examples | Disclosure |
|-------|----------|------------|
| Critical | Manifest forge, key compromise, public index poison | Ack ≤72h; full ≤30d unless logged exemption |
| High | Significant free-core integrity/availability failure | Ack ≤72h |
| Medium | Partial degradation | Register + periodic |
| Low | Cosmetic | Optional batch |

Transparency-system failures use the **same** ladder as model failures.

## Procedure — open an incident

1. Classify severity using `SEVERITY_THRESHOLDS.md`.
2. Append `registers/incidents/INCIDENT_LOG.md` (ID, identified, disclosed, category, summary, status).
3. If High/Critical: follow `docs/handbook/incident/01-high-critical-playbook.md` immediately.
4. Security exemption for withheld technical detail: time-limited, logged, renewable — see `SECURITY_EXEMPTION_PROCESS.md`. **No permanent secrecy.**
5. Post-mortem for high severity: use template under artefacts/05 when present; store in `registers/incidents/`.
6. Stream event if public proof surfaces affected.
7. Update master scorecard Domain 5 if process gaps found.

## Commands (integrity examples)
```bash
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
python3 scripts/oneshot_verify_all.py
python3 scripts/redteam_nano_harness.py
```

## Timeline
| Step | High/Critical |
|------|----------------|
| Initial public/internal ack | ≤72 hours of confirmation |
| Fuller technical disclosure / post-mortem | ≤30 days unless logged exemption |
| Exemption review | On stated expiry; must renew or publish |

## RACI
Incident Response Owner R; leadership bound by policy; may not overrule disclosure except via logged exemption.

## Related drills
- `registers/incidents/TABLETOP_2026-08-08.md`
- `docs/handbook/incident/03-tabletop-drill.md`
