# Paid layers (turn 18)

**Source:** founding conversation ASSISTANT turn 18

Here are the realistic paid layers that sit cleanly around a free TTLLM + ttlink core:

### 1. Hosted / Managed Infrastructure
- Reliable, high-throughput access to the transparent models
- Dedicated capacity, private networking, SLAs, uptime guarantees
- Higher rate limits and priority inference
- Customers pay for performance and reliability, not for access to the model itself

### 2. Enterprise ttlink & Provenance Tools
- Richer interfaces on top of the public ttlink system
- Long-term retention of query + source linkages
- Compliance-grade export formats (audit packs, signed provenance reports)
- Integration into existing enterprise governance / GRC systems
- Private indexing of a customer’s own additional data while still linking back to the public TTLLM skeleton

### 3. Certified / Supported Fine-tunes
- Domain-specific or task-specific versions that inherit the full transparency guarantees
- Commercial support, indemnification, and update paths
- Still fully inspectable (the fine-tune process and data mixture remain visible), but the hosted or supported version is paid

### 4. Transparency-as-a-Service / Methodology
- Helping other organisations apply the same “down to the bone” standard to their own models
- Data release pipelines, checkpointing standards, ttlink implementation, cryptographic provenance setup
- Consulting + implementation work

### 5. Advanced Analysis & Visualisation Products
- Powerful search and comparison tools across the public training data and checkpoints
- Custom dashboards, research workbenches, differential analysis between checkpoints
- Aimed at serious researchers, safety teams, regulators, and enterprise AI governance groups

### 6. Priority Support & Professional Services
- Direct engineering support
- Custom evaluation harnesses
- Onboarding and integration help
- Training for internal teams who want to operate at the same transparency standard

### Design rule for all paid layers
None of them are allowed to require the core TTLLM, its training data, intermediate checkpoints, or basic ttlink stream to become closed or degraded.  

The free public skeleton remains the reference implementation and the cultural proof.  
The paid layers sell reliability, convenience, compliance, deeper tooling, and human expertise on top of that open foundation.
