from pathlib import Path
from free_core.release.pipeline import seal_model_tree

def test_seal_nano_if_present():
    root = Path("models/ttllm-nano")
    if not (root / "data").exists():
        return
    out = seal_model_tree(root, version="test", include_ckpts=False)
    assert out["release"]["count"] > 0
    assert out["release"]["merkle_root"]
