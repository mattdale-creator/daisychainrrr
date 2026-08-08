# Domain 8: Boundary Rules Between Public Core and Commercial Layers

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 44)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/08/` · related `registers/`  

---

**8. Boundary Rules Between Public Core and Commercial Layers**  
**TTLLM Total Transparency Specification – Domain 8**

### Purpose of Transparency in This Domain
The entire business model rests on a hard distinction: the public core remains fully transparent and free, while commercial layers may legitimately remain private in defined respects. Without explicit, public, enforceable boundary rules, commercial convenience will gradually pull pieces of the skeleton into opacity.  

This domain exists to make the boundary itself visible and stable so that both insiders and outsiders can see exactly what is allowed to be private, what must remain public, and how conflicts are resolved.

### Concrete Artefacts to Be Published

1. **Public/Commercial Boundary Specification**  
   - Definitive public document stating what belongs to the free public core and what may reside in commercial layers.  
   - Covers models, data, checkpoints, indexes, ttlink functionality, cryptographic manifests, evaluation artefacts, and infrastructure.  
   - Versioned and signed.

2. **Boundary Decision Log**  
   - Subset of the main Decision Log (Domain 1) or dedicated register that records every significant decision affecting the boundary, including proposals that were rejected.  

3. **Allowed Commercial Privacy List**  
   - Explicit enumeration of the categories of information and artefacts that commercial layers are permitted to keep private (e.g., individual customer data, private fine-tune weights under certain conditions, internal commercial metrics, non-public commercial evaluations).  

4. **Prohibited Opacity List**  
   - Explicit enumeration of what commercial layers are forbidden from making opaque or from requiring the public core to make opaque.  

5. **Periodic Boundary Attestation**  
   - At least annual signed statement confirming that current commercial offerings comply with the published Boundary Specification.

### Processes

- **Default public rule**: Anything not explicitly placed in the Allowed Commercial Privacy List is treated as belonging to the public core or requiring public justification.  
- **Boundary change process**: Any proposed movement of an artefact or capability from public to commercial privacy (or vice versa) is a material decision that must be logged, justified against the standard, and reflected in an updated Boundary Specification before implementation.  
- **New commercial feature review**: Every new paid offering is checked against the Boundary Specification before launch. Features that would require closing part of the public core are rejected.  
- **Conflict resolution**: When commercial incentives push against the boundary, the public core and the Boundary Specification take precedence. This rule is itself public.  
- **Review cadence**: Quarterly internal compliance check; annual public attestation and review of the Specification.

### Roles and Responsibilities

- **Boundary Custodian**: Accountable for the accuracy of the Boundary Specification, the Allowed/Prohibited lists, and the Periodic Attestation.  
- **Commercial product owners**: Responsible for ensuring their offerings stay inside the Allowed Commercial Privacy List and for surfacing any boundary pressure early.  
- **Public-core technical leads**: Empowered and obligated to challenge commercial proposals that risk the boundary.  
- **Leadership / governance body**: Bound by the published rule that commercial features may not require opacity in the public core; may not quietly override it.

### Technical and Legal Mechanisms

- Boundary Specification and related lists maintained in the signed public repository system.  
- Technical separation (infrastructure, access controls, key management) between public-core systems and commercial tenant systems, as already required by the commercial-arm hardening approach.  
- Customer and partner contracts reviewed to ensure they contain no clauses that would force the organisation to violate the Boundary Specification.  
- Release and product-launch checklists include an explicit boundary-compliance step.

### Interaction with Free Core and Commercial Layers

- This domain is the primary interface definition between the two sides of the business model.  
- The free core is protected by the Prohibited Opacity List and the precedence rule.  
- Commercial layers receive clear, stable permission to operate with legitimate privacy inside the Allowed Commercial Privacy List.  
- Revenue goals are not permitted to redefine the boundary after the fact.

### Genuine Tensions and Trade-offs

- **Commercial flexibility vs. hard boundary**: A strict published boundary reduces the ability to opportunistically move features or data into private commercial offerings. This constraint is deliberate.  
- **Customer expectations**: Some enterprise customers will request forms of exclusivity or opacity that violate the boundary. Such requests must be refused.  
- **Evolution pressure**: As the technology and market change, there will be repeated pressure to redraw the line. Each redraw must go through the full public process rather than informal adjustment.  
- **Definitional edge cases**: Certain artefacts (e.g., commercial fine-tunes that still inherit transparency guarantees) sit near the boundary and require careful, case-by-case logging to avoid gradual erosion.

### Implementation Sequence

1. Draft and publish the initial Public/Commercial Boundary Specification together with the Allowed Commercial Privacy List and Prohibited Opacity List.  
2. Establish the Boundary Decision Log (or integrate it tightly with Domain 1).  
3. Audit all existing and planned commercial offerings against the Specification.  
4. Embed boundary review into product development and release processes.  
5. Issue the first Periodic Boundary Attestation.  
6. Include boundary integrity in ongoing governance and red-team reviews.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
