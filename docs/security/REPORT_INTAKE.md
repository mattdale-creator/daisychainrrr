# Security / transparency report intake

**Contact:** md@0265.au  
**security.txt:** https://ttllms.com/security.txt (also `site/security.txt`)  
**Clocks:** Domain 5 (incidents) + Domain 10 (red-team findings)

## In scope (constructive QA)
- Free public core integrity: manifests, seals, signatures, stream chains
- ttlink index poisoning, canary evasion, QueryGuard bypass that enables destructive bulk harm
- Site/deploy paths that falsely claim green verify
- Process failures: missing decision logs, BOUNDARY theater
- Model claims that outrun eval honesty packs

## Out of scope (for this intake)
- Social engineering of individuals
- Physical attacks
- Demands to close free public core
- Illegal content hosting requests

## How to report
1. Email md@0265.au with:
   - Component (manifest / ttlink / stream / site / process / model)
   - Severity guess (Critical / High / Medium / Low)
   - Repro steps, commit SHA or merkle root if known
   - Whether exploit detail should be time-limited (request exemption)
2. We acknowledge High/Critical on Domain 5 clock (≤72h target once confirmed).
3. Findings enter `registers/redteam/FINDINGS_REGISTER.md` and/or `registers/incidents/INCIDENT_LOG.md`.
4. Default: **publish**. Permanent suppression forbidden. Time-limited detail withhold only with expiry.

## Safe harbor intent (not legal advice)
Good-faith research that does not destroy production data, does not extort, and follows this intake is welcomed. We will not pursue researchers for reporting integrity flaws in public artefacts when conducted responsibly. Formal legal safe-harbor language requires entity counsel (human gate).

## SLA summary
| Class | Initial register | Fuller write-up |
|-------|------------------|-----------------|
| Critical | ASAP | ≤30d unless exemption |
| High | ≤7 days (findings) / ack ≤72h (incidents) | per Domain 5/10 |
| Medium/Low | batch OK | periodic |

## Related
- `docs/handbook/incident/01-high-critical-playbook.md`
- `docs/handbook/incident/02-redteam-publication.md`
