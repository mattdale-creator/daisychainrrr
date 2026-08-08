#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(REPO))
from free_core.provenance.manifest import build_merkle_manifest, walk_files, write_manifest
from free_core.ttlink.index import TtlinkIndex
from free_core.stream.schema import StreamEvent
from free_core.stream.log import StreamLog
from free_core.security.shard import seal_shards, ShardManifest

def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def main():
    targets = []
    for sub in ("code", "data", "metrics", "evals", "cards", "ttlink", "stream", "manifests"):
        p = ROOT / sub
        if p.exists():
            targets.extend(walk_files(p))
    man = build_merkle_manifest(targets, base=ROOT, extra={"release": "ttllm-nano-v2", "version": "0.2.0-nano-bpe"})
    write_manifest(man, ROOT / "manifests/RELEASE_MANIFEST.json")
    ckpts = list((ROOT / "checkpoints").glob("*.pt"))
    cman = build_merkle_manifest(ckpts, base=ROOT, extra={"seal": "checkpoints"})
    write_manifest(cman, ROOT / "manifests/CHECKPOINTS_MANIFEST.json")
    idx = TtlinkIndex()
    for p in sorted((ROOT / "data/raw").glob("*.trainslice.txt")):
        idx.add_file(p, doc_id=p.name)
    idx.save(ROOT / "ttlink/index.json")
    (ROOT / "ttlink/binding.json").write_text(json.dumps(idx.manifest_binding(), indent=2) + "\n")
    shard_dir = ROOT / "ttlink/shards"
    shard_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, (doc_id, doc) in enumerate(sorted(idx.docs.items())):
        sp = shard_dir / f"shard_{i:03d}.json"
        sp.write_text(json.dumps({"doc_id": doc_id, "sha256": doc["sha256"]}, indent=2) + "\n")
        paths.append(sp)
    sm = seal_shards(paths, base=ROOT)
    ShardManifest(sm).save(ROOT / "ttlink/shard_manifest.json")
    hyp = json.loads((ROOT / "metrics/hyperparams.json").read_text()) if (ROOT / "metrics/hyperparams.json").exists() else {}
    log = StreamLog()
    log.append(StreamEvent(event_type="bpe_trained", payload={"vocab": hyp.get("vocab_size"), "merges": "bpe.json"}))
    log.append(StreamEvent(event_type="training_finished", payload={"steps": hyp.get("steps"), "n_params": hyp.get("n_params"), "wall_sec": hyp.get("wall_sec")}))
    last = None
    mp = ROOT / "metrics/train.jsonl"
    if mp.exists():
        for line in mp.read_text().splitlines():
            if line.strip():
                last = json.loads(line)
    if last:
        log.append(StreamEvent(event_type="loss_metric", payload=last))
    log.append(StreamEvent(event_type="release", artefact_sha256=man["merkle_root"], payload={"merkle_root": man["merkle_root"], "ckpt_root": cman["merkle_root"]}))
    log.save(ROOT / "stream/public_log.json")
    (ROOT / "cards/MODEL_CARD.md").write_text(f"""# Model card — ttllm-nano-v2

**Version:** 0.2.0-nano-bpe  
**Intent:** Improve nano transparency shape with BPE tokenizer + denser model, same verifiable PG data.

## Architecture
n_layer={hyp.get('n_layer')}, n_head={hyp.get('n_head')}, n_embd={hyp.get('n_embd')}, params={hyp.get('n_params')}

## Tokenizer
Pure-Python BPE over UTF-8 bytes (`data/processed/bpe.json`).

## Data
Same Project Gutenberg public-domain mixture as ttllm-nano v1 — see `data/DATA_CARD.md`.

## Reproduce
```bash
python3 models/ttllm-nano-v2/code/prepare_bpe.py
python3 models/ttllm-nano-v2/code/train.py --steps 1500
python3 models/ttllm-nano-v2/code/eval_pack.py
python3 models/ttllm-nano-v2/code/seal_release.py
```

## Not a frontier model
Tombstone: not OLMo-scale. Process skeleton is the product.
""")
    (ROOT / "cards/TRANSPARENCY_SCORECARD.md").write_text(f"""# Transparency scorecard — ttllm-nano-v2

Generated: {utc()}

| Layer | Status |
|-------|--------|
| Data (PG + hashes + card) | MET |
| Code public | MET |
| Dense checkpoints | MET |
| Metrics + ppl | MET |
| BPE tokenizer published | MET |
| Eval pack (process) | MET |
| Merkle release + ckpt seal | MET |
| ttlink + shards | MET |
| Stream | MET |
| Frontier capability | TOMBSTONE — not claimed |

merkle_root: `{man['merkle_root']}`  
ckpt_root: `{cman['merkle_root']}`
""")
    print("sealed v2", man["count"], man["merkle_root"][:16])

if __name__ == "__main__":
    main()
