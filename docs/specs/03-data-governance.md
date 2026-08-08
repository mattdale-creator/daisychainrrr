# Domain 3: Data Governance and Legal Response Process

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 39)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/03/` · related `registers/`  

---

**3. Data Governance and Legal Response Process**  
**TTLLM Total Transparency Specification – Domain 3**

### Purpose of Transparency in This Domain
The public training data is part of the computational skeleton. If legal or other external pressure can cause silent removal, alteration, or selective withholding of data without a visible record, the “down to the bone” claim becomes conditional and therefore false.  

This domain exists to make the organisation’s handling of data rights, contested content, and legal demands itself inspectable. Outsiders must be able to see what was challenged, what changed, why it changed, and what remains.

### Concrete Artefacts to Be Published

1. **Data Governance Policy**  
   - Public document describing how training data is selected, filtered, documented, and versioned.  
   - Includes stated principles for handling copyrighted material, personal data, and high-risk content.  
   - Versioned and signed.

2. **Data Provenance Manifest**  
   - Machine-readable and human-readable record of the major data sources and mixes used in each public model release.  
   - Linked to the cryptographic manifests already required for the free core.

3. **Legal Action and Takedown Log**  
   - Append-only public log of every formal legal demand, takedown request, or equivalent pressure that results in any change to publicly released data or indexes.  
   - Each entry records: date received, nature of the claim (without necessarily publishing the full claimant identity if legally restricted), data or artefacts affected, decision made, rationale, and date of any restoration or further change.

4. **Data Change Log**  
   - Record of every material modification to previously released public data or ttlink indexes, including voluntary corrections, legal removals, and technical fixes.  
   - Distinguishes legal removals from ordinary maintenance.

5. **Periodic Data Governance Report**  
   - Quarterly summary of volume of challenges received, actions taken, outstanding issues, and any systemic patterns.

### Processes

- **Default preservation rule**: Publicly released data remains public. Removal or alteration is an exceptional act that must be logged.  
- **Intake process**: All formal legal demands are recorded in an internal intake system on the day of receipt. A public log entry is created within 14 days if any public artefact is affected (or a placeholder entry noting that a demand is under review).  
- **Decision standard**: Decisions to remove or alter data must be justified against a written internal standard that prioritises maximal preservation of the public skeleton consistent with law.  
- **Restoration bias**: When a legal basis for removal later falls away, restoration to the public corpus is the default and must be logged.  
- **No quiet side channels**: Informal pressure that results in data changes is treated the same as formal legal process and must appear in the log.  
- **Review cadence**: Monthly internal audit of the Legal Action and Data Change logs; quarterly public report.

### Roles and Responsibilities

- **Data Governance Lead**: Owns the Data Governance Policy, Provenance Manifests, and the integrity of the public logs.  
- **Legal Response Owner**: Accountable for timely and accurate entries in the Legal Action and Takedown Log.  
- **Technical custodians of the public data and indexes**: Responsible for implementing logged changes exactly and for ensuring cryptographic manifests remain consistent with the actual released state.  
- **All staff**: Obligation to route any external demand that could affect public data into the formal intake process.

### Technical and Legal Mechanisms

- Legal Action and Data Change logs maintained as signed, append-only repositories with public read access.  
- Technical ability to mark data as “removed for legal reasons” while preserving the cryptographic history of its prior inclusion (tombstoning rather than silent deletion where legally permissible).  
- Legal counsel operating under explicit instructions that the transparency of the response process is itself a core requirement, not an optional courtesy.  
- Contracts with data providers and contractors include acknowledgement of the public logging obligations.

### Interaction with Free Core and Commercial Layers

- The free public core is the primary object of protection. Any legal response that affects public training data, checkpoints, or ttlink indexes must follow this domain’s full process.  
- Commercial layers may maintain private customer data under ordinary confidentiality. However, if a commercial activity creates legal pressure that threatens the public core, that pressure and the organisation’s response must still be logged.  
- No commercial agreement may contain clauses that require silent alteration of the public skeleton.

### Genuine Tensions and Trade-offs

- **Legal risk vs. transparency**: Publishing the existence and general nature of legal demands can itself create exposure or invite further claims. This elevated surface area is accepted as inherent to the standard.  
- **Claimant privacy / safety**: In limited cases (e.g., individuals at personal risk) full public detail may be restricted. Any such restriction must itself be logged with reason and scope.  
- **Speed of response**: Thorough logging and internal deliberation can slow compliance with time-sensitive legal demands. Operational processes must be designed to meet legal deadlines while still producing the required public record.  
- **Scope of “data”**: Determining what counts as a material change (exact document removal vs. re-filtering vs. index-only changes) requires clear internal definitions to avoid under-logging.

### Implementation Sequence

1. Publish the initial Data Governance Policy.  
2. Stand up the signed Legal Action and Data Change logs.  
3. Ensure all current public data releases have corresponding Provenance Manifests.  
4. Begin logging from the policy effective date forward.  
5. Issue the first quarterly Data Governance Report.  
6. Include this domain in regular integrity and red-team reviews.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
