# Key inventory

| Key | Purpose | Prod trust? | Location | Status |
|-----|---------|-------------|----------|--------|
| examples/keys demo | Tutorial sign/verify | **No** | repo examples | published tutorial |
| ttllm-prod | Free-core release signatures | Yes (future) | not issued | TOMBSTONE |
| Cloudflare API token | Deploy/DNS | n/a (ops) | secrets.local.env gitignored | human-managed |
| GitHub push token | git | n/a | local agent/OS | lacks workflow scope |

**Rule:** Never commit private keys. Rotate on suspicion (Domain 5).
