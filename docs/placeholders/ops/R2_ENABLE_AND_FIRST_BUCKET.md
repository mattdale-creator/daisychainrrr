# R2 enable + first public object — full operator pack

> **Written by Grok - Human checking required**  
> Infra voice. **Hard gate T2** until product enabled.  
> Free-core objects only; tenant data never in public bucket.

---

## 1. Why R2 (ethos)

Git cannot be the sole distribution path for large public weights/shards. Object storage must still be content-addressed: every public object has SHA-256 in a manifest leaf. Paywalling downloads of claimed free-core objects is prohibited opacity.

---

## 2. Enable steps

1. Cloudflare dashboard → account → **R2**  
2. Accept enablement / billing if prompted  
3. Confirm API no longer returns 10042-class enable errors  
4. Create API credentials only in gitignored secrets  

---

## 3. Bucket design

| Field | Value |
|-------|--------|
| Name | `ttllm-public-releases` |
| Purpose | Free-core weights, docs, shard packs |
| Public access | Deliberate; free-core eligible only |
| Versioning | On |
| Forbidden | Customer prompts, tenant weights, secrets |

Key layout: `releases/<model>/<version>/<file>`

---

## 4. First object procedure

```bash
echo "TTLLM free core object — hello" > /tmp/ttllm-r2-hello.txt
sha256sum /tmp/ttllm-r2-hello.txt
npx wrangler r2 object put ttllm-public-releases/releases/bootstrap/hello.txt \
  --file=/tmp/ttllm-r2-hello.txt --remote
```

Record in supply-chain or release card: object key, sha256, date, free-core eligible: yes.

---

## 5. Integrity rules

- Manifest or DATA_CARD must list hash  
- Unpaid GET for public free-core objects  
- Domain 3 process for withdrawal  
- Update ASSET_INVENTORY  

---

## 6. Close T2 only when

R2 enabled + test object uploaded + hash recorded + inventory updated.

---

*Written by Grok - Human checking required — also on https://ttllms.com/placeholders/*
