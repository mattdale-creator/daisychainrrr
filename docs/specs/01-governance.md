# Domain 1: Governance and Decision-Making

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 37)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/01/` · related `registers/`  

---

**1. Governance and Decision-Making**  
**TTLLM Total Transparency Specification – Domain 1**

### Purpose of Transparency in This Domain
Governance is the highest-leverage place soft tissue can hide. If major decisions about what is trained, what is released, what is commercialised, or how conflicts between transparency and other pressures are resolved remain opaque, the organisation can claim radical honesty while still operating with a private decision layer.  

Public, verifiable governance exists to make the organisation’s own generating process as inspectable as the models it produces. Outsiders (and future insiders) must be able to see how power is exercised and how the “down to the bone” standard is protected or compromised in practice.

### Concrete Artefacts to Be Published

1. **Decision Log (primary artefact)**  
   - Append-only, publicly readable log of all significant decisions.  
   - Each entry contains: date, decision title, options considered, rationale, dissenting views (if any), final outcome, and names or roles of decision-makers.  
   - Categories that must be logged: model training priorities, data inclusion/exclusion, commercial feature boundaries, major resource allocation, changes to transparency policy, and responses to external pressure.

2. **Governance Charter**  
   - Short public document defining decision rights, escalation paths, and the non-negotiable rule that commercial features may never require the public core to become opaque.  
   - Versioned and signed.

3. **Meeting Records for Material Decisions**  
   - For any meeting that produces a logged decision: agenda, attendees, and a concise summary of discussion points. Full transcripts optional but preferred when feasible.  
   - Redaction only for genuine personal privacy or active security matters, with the redaction itself logged and justified.

4. **Periodic Governance Transparency Report**  
   - Quarterly public summary of decision volume, categories, any policy changes, and known gaps or delays in logging.

### Processes

- **Default public rule**: Every material decision is presumed public unless a specific, time-limited exception is formally recorded in the Decision Log with a stated reason and expiry.  
- **Decision threshold**: Any decision that affects the public core, the boundary with commercial layers, training runs above a defined compute threshold, or the transparency standard itself must be logged within 7 days.  
- **Dissent capture**: Explicit process for recording minority or dissenting views without requiring consensus theatre.  
- **Exception handling**: Temporary non-publication (e.g., active legal or security matters) must be logged as an exception, including the reason and the date the full record will be released or reviewed.  
- **Review cadence**: Monthly internal audit of the Decision Log for completeness; quarterly public attestation.

### Roles and Responsibilities

- **Governance Custodian** (rotating or dedicated role): Responsible for the integrity and timely publication of the Decision Log and Charter.  
- **Decision owners**: Every logged decision must name the accountable role or person.  
- **All staff and contractors**: Obligation to flag decisions that appear to meet the materiality threshold but have not been logged.  
- **Board / ultimate governing body** (if one exists): Bound by the same logging requirements; their decisions are not exempt.

### Technical and Legal Mechanisms

- Decision Log implemented as a signed, append-only repository (git + cryptographic signatures or equivalent transparency log).  
- Public web interface and machine-readable feed (JSON/CSV) for the log.  
- Legal review limited to confirming that publication does not create immediate, concrete legal jeopardy; legal preference for secrecy is not sufficient grounds for permanent non-publication.  
- Employment and contractor agreements include explicit acceptance of the public decision-logging requirement.

### Interaction with Free Core and Commercial Layers

- Decisions about the free public core (training, data, ttlink, releases) are held to the highest logging standard.  
- Decisions about commercial products must still be logged, with particular attention to any potential impact on the public core or the boundary rules.  
- The commercial arm cannot maintain a parallel private decision system for matters that affect the overall organisation’s transparency posture.

### Genuine Tensions and Trade-offs

- **Speed vs. documentation**: High-tempo technical work can make thorough contemporaneous logging feel costly. Mitigation: lightweight templates and clear materiality thresholds so only significant decisions are fully logged.  
- **Candour vs. interpersonal friction**: Publishing dissent and real rationales can create internal discomfort. This is accepted as the cost of removing soft tissue.  
- **Legal exposure**: Full transparency of decision-making can create discoverable records. The organisation accepts elevated legal surface area as inherent to the chosen standard.  
- **Early-stage pragmatism**: In the first 6–12 months, some process imperfections are expected; they must be publicly acknowledged rather than hidden.

### Implementation Sequence

1. Draft and publish the Governance Charter.  
2. Stand up the signed Decision Log infrastructure.  
3. Begin logging all material decisions from that date forward (no requirement to reconstruct full history before the policy existed, but any reconstruction that is done must be accurate).  
4. Publish the first quarterly Governance Transparency Report.  
5. Include compliance with this domain in the organisation’s internal red-teaming and integrity reviews.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
