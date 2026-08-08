# Domain 7: Supply-Chain and Dependency Transparency

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 43)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/07/` · related `registers/`  

---

**7. Supply-Chain and Dependency Transparency**  
**TTLLM Total Transparency Specification – Domain 7**

### Purpose of Transparency in This Domain
Models and transparency systems do not exist in isolation. They depend on hardware, cloud providers, networking, external software libraries, data-processing tools, signing infrastructure, and other third parties. Hidden or poorly documented dependencies create soft tissue: unexamined points of control, failure, or influence that sit beneath the public skeleton.  

This domain exists to make the material and computational supply chain visible so that the full generating and operating environment of the TTLLM system can be assessed.

### Concrete Artefacts to Be Published

1. **Dependency Register**  
   - Public inventory of material third-party dependencies used in training, inference, ttlink indexing, cryptographic signing, and public serving.  
   - Categories include: cloud / compute providers, hardware platforms, critical open-source libraries, data-pipeline tools, signing and key-management systems, and any proprietary external services.  
   - Updated when material changes occur.

2. **Supply-Chain Risk & Control Summary**  
   - Plain-language description of the major residual risks introduced by key dependencies and the controls in place (contractual, technical, or procedural).  

3. **Compute & Infrastructure Provenance Note**  
   - For each major public model release: statement of the primary compute environment used for training and the significant infrastructure providers involved.  

4. **Change Log for Material Dependencies**  
   - Record of significant additions, removals, or substitutions of dependencies that affect the public core or its verification chain.  

5. **Periodic Supply-Chain Attestation**  
   - At least annual signed statement confirming the Dependency Register is materially complete and accurate.

### Processes

- **Materiality threshold**: Dependencies that can affect model training outcomes, the integrity of public data or indexes, the cryptographic verification chain, or the availability of the public ttlink system are considered material and must appear in the Register.  
- **Default disclosure**: Material dependencies are public. Non-disclosure requires a logged, time-limited justification (e.g., active security constraint).  
- **New dependency review**: Before a material new dependency is adopted for the public core, its inclusion is assessed against transparency impact and recorded.  
- **Incident linkage**: Supply-chain failures or compromises that affect the public core are handled under the Incident & Failure Disclosure Policy (Domain 5) and cross-referenced here.  
- **Review cadence**: Quarterly internal verification of the Register; annual public attestation.

### Roles and Responsibilities

- **Supply-Chain / Infrastructure Lead**: Accountable for the completeness and accuracy of the Dependency Register and related artefacts.  
- **Technical owners of training, indexing, and serving systems**: Responsible for surfacing material dependencies used in their systems.  
- **Security / Red-Team function**: Periodically tests whether undeclared or under-documented dependencies exist.  
- **Leadership**: Ensures commercial or convenience-driven infrastructure choices do not create hidden dependencies that undermine the public standard.

### Technical and Legal Mechanisms

- Dependency Register maintained as a signed, version-controlled public document or repository.  
- Where possible, software dependency information is generated from actual build and runtime manifests rather than manual lists.  
- Contracts with critical providers reviewed for clauses that would prevent disclosure of the relationship or create hidden control rights; such clauses are treated as adverse.  
- Cryptographic signing and key-management dependencies receive heightened scrutiny because they underwrite the verification chain for all other transparency artefacts.

### Interaction with Free Core and Commercial Layers

- All material dependencies of the free public core, ttlink system, and cryptographic provenance infrastructure must be disclosed.  
- Commercial layers may use additional private infrastructure. However, any dependency that is shared with or can affect the public core remains subject to full disclosure.  
- Commercial agreements must not introduce supply-chain opacity into the public skeleton.

### Genuine Tensions and Trade-offs

- **Provider sensitivity**: Some infrastructure providers dislike public listing or detailed risk discussion. This may limit options or require accepting higher-cost alternatives that tolerate disclosure.  
- **Security through obscurity pressure**: There is often internal or external pressure to hide details of security-relevant infrastructure. Under this standard, such hiding is allowed only via the formal, time-limited exemption process and must be logged.  
- **Practical completeness**: Modern systems have deep transitive dependency trees. The requirement focuses on material dependencies rather than every recursive library, while still pushing toward maximal useful visibility.  
- **Changing infrastructure**: Rapid changes in compute providers or tooling can make the Register lag. Operational discipline is required to keep it current.

### Implementation Sequence

1. Create and publish the initial Dependency Register covering current critical systems.  
2. Publish the first Supply-Chain Risk & Control Summary.  
3. Establish the Change Log and materiality criteria.  
4. Integrate dependency disclosure into the model-release and infrastructure-change checklists.  
5. Issue the first Periodic Supply-Chain Attestation.  
6. Include supply-chain visibility in ongoing integrity reviews and red-teaming.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
