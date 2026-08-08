# Domain 5: Incident, Failure, and Red-Team Disclosure Policy

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 41)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/05/` · related `registers/`  

---

**5. Incident, Failure, and Red-Team Disclosure Policy**  
**TTLLM Total Transparency Specification – Domain 5**

### Purpose of Transparency in This Domain
Incidents, failures, and red-team findings are among the strongest tests of whether an organisation actually lives by radical transparency. Most organisations disclose selectively, delay inconvenient findings, or bury internal adversarial results.  

Under the “down to the bone” standard, the organisation must pre-commit to a clear disclosure regime so that the handling of failures is itself inspectable and not subject to post-hoc narrative management. This covers both model behaviour failures and failures of the transparency infrastructure (ttlink, cryptographic manifests, public data integrity, etc.).

### Concrete Artefacts to Be Published

1. **Incident & Failure Disclosure Policy**  
   - Public, versioned document stating what categories of incidents and findings will be disclosed, on what timeline, and with what level of technical detail.  
   - Explicitly covers model issues, transparency-system issues, security incidents affecting the public core, and material red-team results.

2. **Public Incident Log**  
   - Append-only log of all material incidents and failures that meet the disclosure threshold.  
   - Each entry includes: date identified, date disclosed, category, summary of impact, root-cause analysis (when complete), remediation actions, and links to related technical artefacts.

3. **Red-Team Findings Register**  
   - Public register of significant red-team or adversarial findings against the models or the transparency systems.  
   - Distinguishes between findings that have been fully remediated, partially remediated, and accepted as residual risk.  
   - Technical detail is maximised consistent with not creating immediate active exploit risk.

4. **Post-Mortem Archive**  
   - Full post-mortem documents for high-severity incidents, published after an initial short containment window if necessary.

5. **Periodic Integrity & Adversarial Report**  
   - At least semi-annual public summary of incident volume, red-team activity, open residual risks, and any policy changes.

### Processes

- **Pre-committed thresholds**: Clear internal definitions of what constitutes a material incident or significant red-team finding that triggers public disclosure. These thresholds are themselves public.  
- **Timeline rules**:  
  - Initial public acknowledgement of material incidents within a defined short window (e.g., 72 hours of confirmation).  
  - Fuller technical disclosure and post-mortem within a longer defined window (e.g., 30 days), unless an active security exemption is formally invoked and logged.  
- **Security exemption process**: Temporary withholding of specific technical details is permitted only when immediate active exploitation risk exists. Any such exemption must be logged with reason and an expected review date. Exemptions are time-limited and require active renewal.  
- **No selective silence**: Findings that are inconvenient or reputationally damaging are subject to the same rules as neutral or positive findings.  
- **Dual coverage**: The process applies equally to failures of the models and failures of the transparency systems (index integrity, manifest mismatches, ttlink errors, etc.).

### Roles and Responsibilities

- **Incident Response Owner**: Accountable for correct classification, timely logging, and disclosure according to policy.  
- **Red-Team Lead / Adversarial Function**: Responsible for ensuring significant findings enter the disclosure process and are not informally suppressed.  
- **Transparency Custodian**: Monitors that transparency-system failures are treated with the same rigour as model failures.  
- **Leadership**: Bound by the policy; may not overrule disclosure requirements except through the formal, logged exemption process.

### Technical and Legal Mechanisms

- Incident Log and Red-Team Findings Register maintained as signed, append-only public repositories.  
- Internal incident-management system configured so that material events cannot be closed without a corresponding public-log decision.  
- Legal review may advise on wording and timing but cannot impose permanent non-disclosure of material findings without invoking the formal exemption process.  
- Cryptographic linkage where possible between incident reports and affected model checkpoints, data versions, or index versions.

### Interaction with Free Core and Commercial Layers

- All material incidents affecting the free public core, ttlink system, or cryptographic provenance follow the full disclosure policy.  
- Commercial-layer incidents that have no impact on the public skeleton may follow a more restricted disclosure regime appropriate to customer confidentiality. However, any commercial incident that affects or risks the public core is subject to the public policy.  
- Red-teaming of commercial systems is encouraged; findings that reveal systemic issues relevant to the public standard should be surfaced.

### Genuine Tensions and Trade-offs

- **Security vs. transparency**: Immediate full technical disclosure of certain vulnerabilities can enable attacks. The time-limited, logged exemption process is the explicit compromise; permanent secrecy is not permitted.  
- **Reputational cost**: Honest disclosure of failures will be used by critics. This cost is accepted as inherent to the standard.  
- **Internal chilling effect**: Staff may become reluctant to run aggressive red-team tests or report problems if results will be public. Mitigation requires cultural reinforcement that finding and disclosing issues is high-status behaviour.  
- **Volume management**: High-frequency low-severity findings can create noise. Clear materiality thresholds are required to keep the public logs useful rather than overwhelming.

### Implementation Sequence

1. Draft and publish the Incident & Failure Disclosure Policy with explicit thresholds and timelines.  
2. Stand up the signed Public Incident Log and Red-Team Findings Register.  
3. Define the formal security-exemption process and logging requirements.  
4. Apply the policy to all new incidents and findings from the effective date.  
5. Publish the first Periodic Integrity & Adversarial Report.  
6. Include compliance with this domain in ongoing internal audits and meta-red-teaming of the organisation itself.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
