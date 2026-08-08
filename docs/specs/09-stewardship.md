# Domain 9: Stewardship and Continuity

**Status:** Normative implementation plan (founding conversation ASSISTANT turn 45)  
**Source:** *Totally Transparent LLMs: OLMo and LLM360*  
**Ethos:** down to the bone · free public core · verifiable process  

**Operational dirs:** `docs/specs/artefacts/09/` · related `registers/`  

---

**9. Stewardship and Continuity**  
**TTLLM Total Transparency Specification – Domain 9**

### Purpose of Transparency in This Domain
The public core only has lasting value if it remains available and verifiable beyond the current organisation’s goodwill or existence. Acquisition, insolvency, leadership change, or strategic pivot can otherwise turn a transparent skeleton into a proprietary or abandoned artefact.  

This domain exists to pre-commit the organisation to continuity mechanisms so that the public models, data, indexes, cryptographic manifests, and verification tools cannot be silently withdrawn or closed. Stewardship rules must themselves be public and robust to organisational change.

### Concrete Artefacts to Be Published

1. **Continuity & Stewardship Covenant**  
   - Public, versioned legal and policy document stating the organisation’s binding commitments regarding the long-term availability and openness of the public core.  
   - Covers models, training data, intermediate checkpoints, ttlink indexes, cryptographic manifests, and verification tooling.  
   - Signed by the governing body.

2. **Public Core Asset Inventory**  
   - Maintained list of the specific artefacts that fall under continuity protection.  
   - Linked to cryptographic manifests.

3. **Succession & Failure Mode Plan**  
   - Public description of what happens to the public core in defined scenarios: acquisition, insolvency, dissolution, or material change of control.  
   - Identifies intended successor mechanisms (e.g., escrow, foundation, multi-party stewardship, automatic public release triggers).

4. **Key & Signing Continuity Design**  
   - Description of how root cryptographic keys and signing authority for the public verification chain are protected against single-organisation failure or capture.

5. **Periodic Continuity Attestation**  
   - At least annual signed confirmation that the Continuity Covenant remains in force and that technical and legal arrangements are still adequate.

### Processes

- **Pre-commitment rule**: Continuity arrangements must be established and publicly documented before or simultaneous with major public releases, not invented after a crisis.  
- **Change-of-control triggers**: Defined events (acquisition, change of majority ownership, insolvency filings, etc.) automatically activate continuity measures. These triggers are public.  
- **No unilateral withdrawal**: The organisation commits not to withdraw or close already-released public-core artefacts except under the narrow, logged legal processes defined in Domain 3.  
- **Successor evaluation**: Any proposed transfer of stewardship is subject to public notice and must preserve the “down to the bone” standard.  
- **Review cadence**: Annual review of legal instruments, technical escrow/backup arrangements, and key-management continuity; public attestation follows.

### Roles and Responsibilities

- **Stewardship Custodian**: Accountable for the maintenance of the Continuity Covenant, Asset Inventory, and technical continuity arrangements.  
- **Governing body / Board**: Ultimately responsible for ensuring the Covenant is legally robust and not quietly weakened.  
- **Technical leads for data, indexes, and cryptography**: Responsible for the practical implementability of continuity (backups, escrow deposits, key-sharing or multi-signature designs).  
- **Legal counsel**: Tasked with keeping continuity instruments enforceable across relevant jurisdictions.

### Technical and Legal Mechanisms

- Legal instruments (Covenant, escrow agreements, multi-party stewardship contracts, or foundation charters) drafted to survive change of control where possible.  
- Technical continuity measures: regular deposits of public-core artefacts and verification material into independent escrow or multi-party controlled storage; documented recovery procedures.  
- Cryptographic continuity: root signing keys structured (multi-signature, threshold, or social-recovery style arrangements) so that no single future organisation can unilaterally rewrite the verification chain.  
- Public Core Asset Inventory kept in the signed repository system and cryptographically linked to the actual artefacts.

### Interaction with Free Core and Commercial Layers

- Continuity protections apply primarily and non-negotiably to the free public core.  
- Commercial-layer assets (customer data, private fine-tunes, proprietary commercial tooling) follow ordinary commercial continuity practices and are not automatically subject to the same public-stewardship rules.  
- No commercial transaction or funding agreement may contain terms that nullify or override the Continuity Covenant with respect to the public core.

### Genuine Tensions and Trade-offs

- **Legal fragility**: Continuity commitments can be difficult to make fully bankruptcy-proof or acquisition-proof in every jurisdiction. The organisation must be honest about residual legal risk rather than over-claiming.  
- **Key-management complexity**: Robust cryptographic continuity (threshold signatures, multi-party control) adds operational overhead and new failure modes. This cost is accepted.  
- **Successor quality risk**: Transferring stewardship to another entity does not guarantee the successor will maintain the same standard. Public triggers and Covenant terms can reduce but not eliminate this risk.  
- **Early-stage practicality**: In the first years, full legal and technical continuity arrangements may be incomplete. Any gaps must be publicly acknowledged and given explicit closure timelines.

### Implementation Sequence

1. Draft and publish the Continuity & Stewardship Covenant.  
2. Create the Public Core Asset Inventory and link it to existing cryptographic manifests.  
3. Design and document the Key & Signing Continuity approach.  
4. Establish initial technical escrow or multi-party backup arrangements for critical public artefacts.  
5. Define and publish change-of-control triggers.  
6. Issue the first Periodic Continuity Attestation.  
7. Include continuity readiness in regular governance and integrity reviews.

This domain is now specified at a level that can be dropped directly into a master TTLLM Transparency Specification.
