# Domain 10: Red-Team Findings Publication Standard

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 46)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/10/` · related `registers/`  

---

**10. Red-Team Findings Publication Standard**  
**TTLLM Total Transparency Specification – Domain 10**

### Purpose of Transparency in This Domain
Red-teaming is only meaningful under a radical transparency standard if the significant results are themselves visible. Hidden adversarial findings recreate soft tissue: the organisation can claim rigorous testing while selectively suppressing inconvenient or reputationally costly results.  

At the same time, immediate full publication of every exploit detail can create active security harm. This domain exists to define a clear, pre-committed standard for what red-team findings are published, at what level of detail, and on what timeline, so that disclosure is systematic rather than discretionary.

### Concrete Artefacts to Be Published

1. **Red-Team Publication Standard**  
   - Public, versioned policy stating the classification of findings, required disclosure timelines, permitted redaction grounds, and the format of public reports.  
   - Explicitly covers findings against models, ttlink systems, cryptographic provenance infrastructure, and related public systems.

2. **Public Red-Team Findings Register**  
   - Append-only register of all significant findings that meet the disclosure threshold.  
   - Each entry includes: unique identifier, date discovered, date published, affected component (model checkpoint, index version, etc.), severity classification, summary of the issue, remediation status, and residual risk statement.

3. **Detailed Finding Reports**  
   - Technical write-ups for significant findings, published at the level of detail permitted by the Standard.  
   - Where full exploit details are temporarily withheld, the report states what is withheld and under which exemption.

4. **Remediation & Residual Risk Tracker**  
   - Public tracking of whether each registered finding has been fully fixed, partially mitigated, or accepted as residual risk, with dates and supporting evidence where possible.

5. **Periodic Red-Team Activity Summary**  
   - At least semi-annual public summary of red-team effort, volume of findings by category, open residual risks, and any changes to the Publication Standard itself.

### Processes

- **Classification on discovery**: Every red-team finding is classified against published severity and disclosure-threshold criteria. Classification decisions are themselves reviewable.  
- **Default publication rule**: Significant findings are published. Non-publication or heavy redaction requires a formal, logged exemption.  
- **Timeline requirements**:  
  - Initial register entry within a short defined window after confirmation.  
  - Fuller technical report within a longer defined window, subject only to active security exemptions.  
- **Security exemption process**: Temporary withholding of specific technical details is allowed only when there is concrete, immediate exploitation risk. Exemptions are time-limited, require justification, and must be revisited. Permanent suppression is not permitted.  
- **Remediation linkage**: Publication is not delayed solely because remediation is incomplete. Findings are published with their current remediation status.  
- **Scope**: Applies to both externally contracted red-teaming and internal adversarial testing.

### Roles and Responsibilities

- **Red-Team Lead / Adversarial Function**: Accountable for correct classification, timely register entries, and production of public reports according to the Standard.  
- **Incident / Disclosure Owner** (shared with Domain 5): Ensures consistency between incident disclosure and red-team finding disclosure.  
- **Technical owners of affected systems**: Responsible for accurate remediation-status updates and for not obstructing publication.  
- **Leadership**: May not permanently override the Publication Standard; any intervention must use the formal exemption process and be logged.

### Technical and Legal Mechanisms

- Red-Team Findings Register and related reports maintained as signed, append-only public repositories.  
- Cryptographic or version linkage between findings and the specific model checkpoints, data versions, or index versions they affect.  
- Internal red-team tooling and ticketing configured so that significant findings cannot be closed without a public-register decision.  
- Legal review may refine wording and advise on timing but operates inside the pre-committed Standard rather than replacing it.

### Interaction with Free Core and Commercial Layers

- All significant red-team findings against the free public core, ttlink system, cryptographic manifests, or public evaluation infrastructure follow the full Publication Standard.  
- Findings that affect only commercial-layer systems may follow a more restricted disclosure path appropriate to customer confidentiality, provided they have no material impact on the public core.  
- If a commercial-system finding reveals a systemic issue relevant to the public standard, it is surfaced under this domain.

### Genuine Tensions and Trade-offs

- **Security vs. transparency**: The central and permanent tension. The time-limited, logged exemption process is the explicit design response; the organisation accepts that some short-term risk is traded for long-term credibility.  
- **Incentives for red-teamers**: Public attribution and detailed publication can both motivate and deter skilled adversarial testers. Clear rules on credit and on what will be published help manage this.  
- **Volume and signal**: Publishing every low-severity finding can obscure important results. Materiality thresholds are therefore mandatory and themselves public.  
- **Reputational weaponisation**: Detailed public findings will be used by critics and competitors. This cost is accepted as inherent to the standard.

### Implementation Sequence

1. Draft and publish the Red-Team Publication Standard with clear classification criteria, timelines, and exemption rules.  
2. Stand up the signed Public Red-Team Findings Register and Remediation Tracker.  
3. Align internal red-team workflows with the classification and publication requirements.  
4. Begin registering and publishing findings under the new Standard.  
5. Issue the first Periodic Red-Team Activity Summary.  
6. Include compliance with this domain in meta-level integrity reviews and in the organisation’s own adversarial testing of its disclosure processes.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
