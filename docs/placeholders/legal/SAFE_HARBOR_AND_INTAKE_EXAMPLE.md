# Security research safe harbor + intake — full example

> **Written by Grok - Human checking required**  
> Security counsel voice. Formal adoption requires entity counsel (T6). Pre-entity: publish as **intent**.  
> Live operational intake: `docs/security/REPORT_INTAKE.md` · site security-policy · md@0265.au

---

## 1. Purpose (ethos)

Significant findings against models **and** transparency systems must be publishable systematically. Researchers who help prove the skeleton is real should not fear retaliation for good-faith work. Permanent silence is forbidden; time-limited detail withhold needs expiry.

---

## 2. Safe harbor (example site language)

If you make a good-faith effort to comply with this policy during security research against **public free-core artefacts** (manifests, seals, public ttlink indexes, public stream logs, public site integrity claims, public free_core tooling), we will not pursue civil claims for that research or initiate a complaint to law enforcement for accidental, good-faith violations of this policy that occur during research conducted consistent with this text.

### You must
- Report via **md@0265.au** promptly after confirmation  
- Provide repro steps, commit SHA or merkle roots when possible  
- Allow reasonable time before public exploit detail if we request a time-limited Domain 5/10 exemption with **expiry**  
- Not require free-core closure as a condition of disclosure  

### You must not
- Access private customer data or non-public commercial tenant systems  
- Disrupt production availability beyond minimal verification  
- Extort or demand payment  
- Exfiltrate data unrelated to demonstrating the issue  
- Attack third parties unrelated to TTLLM  

### We must
- Classify under Domain 10 / Domain 5  
- Register High+ findings on clock  
- Not permanently suppress High+ free-core integrity findings  
- Publish existence + severity + component even when exploit detail is briefly delayed  

---

## 3. SLA (aligned Domains 5/10)

| Severity | Register / ack target | Fuller write-up |
|----------|----------------------|-----------------|
| Critical | ASAP; incident ack ≤72h once confirmed | ≤30d unless exemption |
| High | Finding ≤7 days; incident ack ≤72h if operational | per standard |
| Medium/Low | Batch OK | periodic |

---

## 4. Scope examples

| In scope | Out of scope |
|----------|--------------|
| Manifest forge / tamper detection failures | Social engineering of individuals |
| Stream chain breaks | Physical attacks |
| Index poison / canary evasion | Demands to close free core |
| False green verify claims | Illegal content hosting requests |
| BOUNDARY theater / decision log gaps | |

---

## 5. Adoption steps for human counsel

1. Localise language to jurisdiction and insurance.  
2. Decide pre-entity “intent” vs post-entity formal policy.  
3. Publish on `security-policy.html` + security.txt Policy URL.  
4. Domain 1 if material.  

---

*Written by Grok - Human checking required — also on https://ttllms.com/placeholders/*
