# Free public core

**Updated:** 2026-08-07

Normative boundary: `commercial/BOUNDARY.md`.

Installable tools: `ttllm-manifest`, `ttllm-ttlink`, `ttllm-stream`.

Seal the repo:

```bash
python3 scripts/build_public_artefacts.py
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
```

Version: free_core 0.2.0
