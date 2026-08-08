# R2 upload runbook (after enable)

1. Confirm R2 enabled in dashboard (wall closed).
2. Create bucket `ttllm-public-releases`.
3. Put credentials in **gitignored** `ops/secrets.local.env` only.
4. Upload free-core artefact + record hash:
```bash
sha256sum path/to/file
npx wrangler r2 object put ttllm-public-releases/releases/<name>/<file> --file=path/to/file
```
5. Update public manifest or DATA_CARD / release card with object key + sha256.
6. Update `continuity/ASSET_INVENTORY.md`.
7. Verify unpaid GET of public object URL (if public).
8. Never upload tenant data to this bucket.
