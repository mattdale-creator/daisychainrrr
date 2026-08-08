# Domain 2: Ownership, Funding, and Influence

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 38)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/02/` · related `registers/`  

---

**2. Ownership, Funding, and Influence**  
**TTLLM Total Transparency Specification – Domain 2**

### Purpose of Transparency in This Domain
Ownership and funding determine who ultimately holds power over the organisation. Hidden cap tables, side letters, preferential rights, or quiet investor influence create soft tissue that can override the “down to the bone” standard when pressure arises.  

Public visibility of ownership, capital sources, and formal influence rights exists so that outsiders can assess whether the organisation’s stated commitment to radical transparency is structurally protected or quietly subordinated to investor interests.

### Concrete Artefacts to Be Published

1. **Cap Table Summary**  
   - Current ownership percentages by named entity or individual (or anonymised role if a natural person requests privacy, with the fact of anonymisation itself disclosed).  
   - Fully diluted view including options, warrants, and convertible instruments.  
   - Updated within 14 days of any material change.

2. **Funding History Log**  
   - Chronological record of every financing round or significant capital contribution: date, amount, instrument type, lead participants, and key terms that affect control or information rights.  
   - Plain-language summary of any rights that could influence technical or release decisions.

3. **Influence Rights Register**  
   - Explicit list of any contractual rights held by investors or other parties that grant board seats, vetoes, information rights, or approval rights over model releases, data practices, or changes to the transparency policy.  
   - Statement when no such rights exist.

4. **Beneficial Ownership Disclosure**  
   - Identification of any ultimate beneficial owners above a defined threshold (e.g., 10% or more on a fully diluted basis), subject only to narrow legal constraints.

5. **Annual Ownership & Influence Attestation**  
   - Signed public statement confirming the published records are complete and accurate as of the attestation date.

### Processes

- **Default disclosure rule**: All ownership and funding information is public unless a specific, narrowly justified exception is recorded.  
- **Change notification**: Any alteration to the cap table, funding instruments, or influence rights must be reflected in the public artefacts within 14 days.  
- **New capital process**: Before accepting new funds, the organisation must publish the proposed key terms that affect control or transparency obligations and allow a short public comment window (or explicitly waive it with recorded justification).  
- **Side-letter prohibition**: Side letters that grant undisclosed rights are forbidden. Any side letter that exists must be published or the relationship terminated.  
- **Review cadence**: Quarterly internal verification; annual public attestation.

### Roles and Responsibilities

- **Ownership Custodian**: Responsible for maintaining the accuracy and timely publication of the Cap Table Summary, Funding History Log, and Influence Rights Register.  
- **Board / Directors**: Personally accountable for the completeness of influence-rights disclosures.  
- **Fundraising lead**: Obligated to ensure no non-public rights are created during capital raises.  
- **All significant equity holders**: Required to cooperate with beneficial-ownership disclosure above the threshold.

### Technical and Legal Mechanisms

- Cap table and funding records maintained in a signed, version-controlled repository with public read access.  
- Legal agreements (SHA, investment agreements, side letters) reviewed specifically for hidden control or information rights; any such rights must be extracted into the public Influence Rights Register.  
- Employment and contractor agreements include acknowledgement that ownership and funding transparency is a condition of the organisation’s standard.  
- Where local law restricts naming of natural persons, the restriction itself and the affected percentage are disclosed.

### Interaction with Free Core and Commercial Layers

- Ownership and influence transparency applies to the entire organisation; there is no separate private ownership structure for the commercial arm.  
- Any investor right that could force opacity on the public core, delay releases, or restrict ttlink functionality is treated as incompatible with the standard and must be rejected or removed.  
- Commercial revenue does not create an alternative power centre that is exempt from these disclosures.

### Genuine Tensions and Trade-offs

- **Investor comfort vs. standard**: Many conventional investors dislike full public cap tables and influence disclosure. This will narrow the pool of compatible capital. Accepted as a filtering mechanism.  
- **Personal privacy of early individuals**: Naming natural-person shareholders can create personal risk. Mitigation: allow limited anonymisation above a high threshold only when legal risk is concrete, with the anonymisation itself logged.  
- **Speed of fundraising**: Public disclosure of terms before closing can complicate negotiations. The process accepts slower fundraising in exchange for structural integrity.  
- **Complex instruments**: Convertible notes, SAFEs, and option pools can obscure real control. The plain-language Influence Rights Register is mandatory to prevent this form of soft tissue.

### Implementation Sequence

1. Publish the current Cap Table Summary and Funding History Log (reconstructing history as accurately as possible).  
2. Create and publish the Influence Rights Register (explicitly stating “none” if applicable).  
3. Embed the disclosure obligations into all future investment documents.  
4. Institute the 14-day update rule and quarterly verification.  
5. Issue the first Annual Ownership & Influence Attestation.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
