# Protect commercial arm (turn 17)

**Source:** founding conversation ASSISTANT turn 17

Here’s how you protect the profit-making arm with the same seriousness, without poisoning the free core.

### 1. Strict isolation (the most important rule)

The commercial systems must be architecturally and operationally separated from the public TTLLM + ttlink core.

- Public core: fully open data, checkpoints, indexes, streams, basic ttlink queries.
- Commercial arm: runs on separate infrastructure, separate identity systems, separate databases, separate signing keys.

A compromise of a paying customer’s environment must not give an attacker the ability to alter the public skeleton, and vice versa.

### 2. What actually needs protecting on the commercial side

| Asset | Risk | Hardening approach |
|-------|------|--------------------|
| Customer data & private fine-tunes | Exfiltration, training-data leakage back into public models | Strong tenant isolation, encryption at rest + in transit, no shared training loops with the public model |
| Enterprise ttlink / audit tooling | Reverse-engineering, IP theft | Keep the advanced tooling closed or source-available under commercial licence; the *public* ttlink remains the reference implementation |
| Hosted inference & dedicated capacity | Abuse, cryptomining, account takeover | Strict auth, per-tenant rate limits, anomaly detection, hardware isolation where needed |
| Billing & entitlement systems | Fraud, privilege escalation | Standard high-assurance practices + cryptographic tokens for feature access |
| Compliance / provenance exports for customers | Forgery of audit trails | Same signed-manifest approach used on the public side, but scoped to the customer’s private artefacts |

### 3. Cryptographic consistency without giving away the commercial edge

You can reuse the same provenance philosophy:

- Every private fine-tune or customer-specific index still gets a signed manifest and content hashes.
- The customer receives the verification keys and can independently check integrity.
- You do **not** publish the private weights or the customer’s data.

This keeps the “down to the bone” standard for the customer while protecting the commercial value.

### 4. Red-teaming the commercial surface

Frontier-level hardening means you also attack your own money-making systems:

- Account takeover and privilege escalation paths
- Cross-tenant data leakage
- Abuse of higher-rate-limit or dedicated endpoints
- Attempts to use commercial APIs to reconstruct or poison the public index
- Social engineering against support and sales staff who have elevated access

The commercial red-team program should be as aggressive as the one aimed at the public transparency layer.

### 5. Business-rule protections (non-code)

- Contracts and acceptable-use policies that explicitly forbid using commercial access to attack or degrade the public core.
- Clear internal policy: no commercial feature is allowed to require closing or weakening the public TTLLM.
- Separate signing keys and release processes so a compromise of commercial signing infrastructure does not let an attacker publish fake public checkpoints or indexes.

### Summary

Protect the profit arm by:

1. Hard isolation from the public core  
2. Applying the same cryptographic provenance standards *inside* each customer’s boundary  
3. Keeping advanced commercial tooling closed while the reference transparency layer stays open  
4. Red-teaming the commercial attack surface with equal intensity  
5. Never letting revenue features require the public skeleton to become opaque

Done this way, the commercial arm can be robust and profitable without turning the original “down to the bone” promise into marketing copy. The free core remains the proof; the paid layers remain the sustainable engine.
