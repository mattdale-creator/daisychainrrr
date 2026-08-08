# Security research safe harbor — example policy language

> **Written by Grok - Human checking required**  
> Written as if by security counsel. Formal adoption requires entity counsel.  
> Live intake: `docs/security/REPORT_INTAKE.md` · md@0265.au

## Safe harbor (example text for site)
If you make a good-faith effort to comply with this policy during security research against **public free-core artefacts** (manifests, seals, public ttlink indexes, public stream logs, public site integrity claims), we will not pursue civil claims for that research or initiate a complaint to law enforcement for accidental, good-faith violations of this policy that occur during research conducted consistent with this text.

You must not:
- Access private customer data or non-public commercial systems  
- Disrupt production availability beyond minimal verification  
- Extort or demand payment  
- Exfiltrate data unrelated to demonstrating the issue  

You must:
- Report via md@0265.au promptly  
- Allow reasonable time before public exploit detail if we request a time-limited Domain 5/10 exemption  
- Not require us to close the free public core as a condition of disclosure  

## Response SLA (aligns Domains 5/10)
| Severity | Initial public/register target |
|----------|--------------------------------|
| Critical | ASAP; incident ack ≤72h once confirmed |
| High | Finding register ≤7 days; incident ack ≤72h if operational |
| Medium/Low | Batch OK |

## Adoption steps for human counsel
1. Localise language to jurisdiction.  
2. Confirm insurance implications.  
3. Publish on security-policy.html after entity exists (or as “intent” pre-entity).  

---
*Written by Grok - Human checking required*
