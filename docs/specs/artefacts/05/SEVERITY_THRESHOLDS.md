# Incident severity thresholds — Domain 5

Transparency-system failures use the **same** ladder as model failures.

| Level | Definition | Examples | Disclosure clock |
|-------|------------|----------|------------------|
| **Critical** | Public skeleton integrity or root-of-trust failure | Manifest forge, production key compromise, public index poison, signed false green | Ack ≤72h of confirmation; fuller ≤30d unless logged exemption |
| **High** | Significant free-core integrity or availability failure | Prolonged false claim on status; seal systematically wrong in public deploy; stream tip rewrite detected late | Ack ≤72h |
| **Medium** | Partial degradation without proven forge | Flaky API, partial scorecard gap, delayed Domain 1 log | Register + periodic summary |
| **Low** | Cosmetic / no integrity impact | Typos, styling, non-claim docs | Optional batch |

## Classification rules
1. If unsure High vs Critical → treat as Critical until lowered with rationale.  
2. “Not yet capital” is **not** an incident; it is a hard-gate tombstone.  
3. Soft-tissue marketing without artefacts → Domain 4 claim-gate failure; promote to Domain 5 if public green was asserted.

## Related
- Playbook: `docs/handbook/incident/01-high-critical-playbook.md`  
- Policy: `INCIDENT_DISCLOSURE_POLICY.md`
