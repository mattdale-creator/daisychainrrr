# Domain 4: Evaluation and Benchmarking Practices

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 40)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/04/` · related `registers/`  

---

**4. Evaluation and Benchmarking Practices**  
**TTLLM Total Transparency Specification – Domain 4**

### Purpose of Transparency in This Domain
Evaluation is one of the most common places soft tissue survives even in otherwise open projects. Selective reporting, private evaluation sets, undisclosed contamination, opaque prompting, and post-hoc methodology changes allow an organisation to present a misleading picture of model capability while still releasing weights and data.  

Under the “down to the bone” standard, the methods used to measure the models must themselves be inspectable. Outsiders must be able to reproduce, audit, and critique the evaluation process with the same rigour they can apply to the training data and checkpoints.

### Concrete Artefacts to Be Published

1. **Evaluation Protocol Document**  
   - Complete description of every benchmark and evaluation procedure used for public claims.  
   - Includes exact prompts, scoring methods, few-shot examples, decoding parameters, and any post-processing.  
   - Versioned and signed for each major model release.

2. **Contamination Analysis Report**  
   - Public analysis of training-data overlap with evaluation sets for every reported benchmark.  
   - Methodology for detecting contamination and quantitative results.  
   - Clear statement of residual risk where detection is imperfect.

3. **Full Evaluation Results Archive**  
   - Machine-readable release of raw evaluation outputs (model generations + scores) for all primary benchmarks, not only summary statistics.  
   - Linked to the specific model checkpoint and evaluation protocol version.

4. **Private / Held-Out Evaluation Register**  
   - Explicit list of any evaluation sets or procedures that are not fully published, with justification and a statement of whether they are used in public capability claims.  
   - Preference is strongly against any private evaluation that supports public claims.

5. **Evaluation Change Log**  
   - Record of every material change to evaluation methodology, prompts, or scoring after initial publication, including rationale.

### Processes

- **Default full-publication rule**: Any evaluation used to support a public claim about model capability must have its protocol, contamination analysis, and raw results published.  
- **Pre-release evaluation freeze**: Evaluation protocols for a given model release are fixed and published before or simultaneous with the model release. Post-hoc changes require an explicit log entry and justification.  
- **Contamination first**: No benchmark result is reported without an accompanying contamination analysis.  
- **Reproducibility package**: For each major release, a public package sufficient for a third party to re-run the primary evaluations is provided (or a clear statement of what is missing and why).  
- **Review cadence**: Evaluation artefacts are reviewed for completeness at every major model release and quarterly thereafter.

### Roles and Responsibilities

- **Evaluation Lead**: Accountable for the completeness and accuracy of the Evaluation Protocol Documents, contamination analyses, and results archives.  
- **Model release owner**: May not make public capability claims that lack corresponding published evaluation artefacts.  
- **Red-team / integrity function**: Periodically attempts to detect undisclosed evaluation practices or contamination under-reporting.  
- **All technical staff**: Obligation to surface any evaluation activity that appears to fall under the public-claim rule but has not been documented.

### Technical and Legal Mechanisms

- Evaluation protocols, raw results, and contamination reports stored in signed, version-controlled public repositories.  
- Cryptographic linkage between model checkpoint hashes, evaluation protocol versions, and result archives.  
- Where third-party benchmarks impose licensing or redistribution restrictions, the restriction itself is disclosed and the organisation’s usage is documented.  
- Automated checks (where feasible) that public claims on the website or papers match published evaluation artefacts.

### Interaction with Free Core and Commercial Layers

- All evaluations of the free public models follow the full transparency requirements above.  
- Commercial fine-tunes and hosted offerings may run additional private evaluations for internal quality control. However, any public claim about those commercial offerings that references capability must still meet the same disclosure standard or be clearly labelled as non-public evaluation.  
- The existence of private commercial evaluations does not relax the requirements for the public core.

### Genuine Tensions and Trade-offs

- **Competitive information**: Full publication of prompts and methodologies can allow others to optimise specifically for the reported evaluations. This is accepted; the standard prioritises inspectability over protecting evaluation “moats.”  
- **Contamination detection limits**: Perfect contamination analysis is often impossible. The requirement is honest, detailed reporting of methods and residual uncertainty, not the pretence of certainty.  
- **Cost and speed**: Rigorous contamination analysis and raw-result publication add engineering overhead to every release. This cost is treated as mandatory rather than optional polish.  
- **Third-party benchmark constraints**: Some widely used benchmarks restrict full redistribution of questions or answers. In such cases the organisation must either avoid relying on them for primary claims or disclose the exact limitations on reproducibility.

### Implementation Sequence

1. Publish the initial Evaluation Protocol Document template and standards.  
2. For the first public model release, produce full protocol, contamination analysis, and results archive.  
3. Establish the Evaluation Change Log and Private Evaluation Register.  
4. Integrate evaluation-artefact completeness into the model release checklist.  
5. Include evaluation transparency in ongoing integrity reviews and red-teaming.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
