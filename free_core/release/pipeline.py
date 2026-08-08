"""Release pipeline helpers: scorecard + seal listing for a model dir."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from free_core.provenance.manifest import build_merkle_manifest, walk_files, write_manifest, verify_manifest
from free_core.release.scorecard import build_scorecard
from free_core.ttlink.index import TtlinkIndex
from free_core.security.canary import inject_canary, check_canary
from free_core.stream.schema import StreamEvent
from free_core.stream.log import StreamLog


def seal_model_tree(model_root: Path, *, version: str, include_ckpts: bool = True) -> dict[str, Any]:
    model_root = Path(model_root)
    repo = model_root.parents[1] if model_root.parent.name == "models" else Path(".")
    targets = []
    for sub in ("code", "data", "metrics", "evals", "cards", "ttlink", "stream", "manifests"):
        p = model_root / sub
        if p.exists():
            targets.extend(walk_files(p))
    man = build_merkle_manifest(targets, base=model_root, extra={"release": model_root.name, "version": version})
    write_manifest(man, model_root / "manifests" / "RELEASE_MANIFEST.json")
    out: dict[str, Any] = {"release": man}
    if include_ckpts and (model_root / "checkpoints").exists():
        ckpts = list((model_root / "checkpoints").glob("*.pt"))
        cman = build_merkle_manifest(ckpts, base=repo, extra={"seal": f"{model_root.name}-ckpts"})
        write_manifest(cman, model_root / "manifests" / "CHECKPOINTS_MANIFEST.json")
        out["checkpoints"] = cman
        out["ckpt_verify"] = verify_manifest(cman, repo)
    # ttlink + canary
    raw = model_root / "data" / "raw"
    if raw.exists():
        idx = TtlinkIndex()
        for p in sorted(raw.glob("*.trainslice.txt")):
            idx.add_file(p, doc_id=p.name)
        inject_canary(idx, "ttllm-public-canary-v1")
        (model_root / "ttlink").mkdir(exist_ok=True)
        idx.save(model_root / "ttlink" / "index.json")
        out["canary"] = check_canary(idx, "ttllm-public-canary-v1")
    return out
