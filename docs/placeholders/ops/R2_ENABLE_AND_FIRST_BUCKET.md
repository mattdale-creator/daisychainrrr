# R2 enable + first public object — operator packet

> **Written by Grok - Human checking required**  
> Written as if by infra lead. **Hard gate T2** until R2 product enabled.

## Enable
1. Cloudflare dashboard → account home → **R2**  
2. Accept enablement / billing acknowledgment if prompted  
3. Confirm API no longer returns 10042 on bucket list  

## Create bucket
| Field | Value |
|-------|--------|
| Name | `ttllm-public-releases` |
| Location | Auto / nearest |
| Public access | Allowed for free-core objects only (configure carefully) |

## First object (example)
```bash
# After credentials in secrets.local.env
echo "TTLLM free core object — hello" > /tmp/ttllm-r2-hello.txt
sha256sum /tmp/ttllm-r2-hello.txt
npx wrangler r2 object put ttllm-public-releases/releases/bootstrap/hello.txt \
  --file=/tmp/ttllm-r2-hello.txt --remote
```

## Integrity
Record in `registers/supply-chain/` or release card:
- object key  
- sha256  
- date  
- “free-core eligible: yes”

## Forbidden
Tenant data, customer prompts, private fine-tune weights, API secrets.

## Close gate
Update `ops/HUMAN_GATES.md` T2 → closed; ASSET_INVENTORY row for bucket.

---
*Written by Grok - Human checking required*
