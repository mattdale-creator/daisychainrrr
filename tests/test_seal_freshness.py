"""Seal freshness and seal_targets unit tests."""
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from free_core.provenance.seal_targets import build_free_core_manifest, collect_seal_targets
from free_core.provenance.manifest import write_manifest, load_manifest


def test_collect_targets_nonempty():
    t = collect_seal_targets(REPO)
    assert len(t) > 10
    assert any(p.name == "BOUNDARY.md" for p in t) or any("BOUNDARY" in str(p) for p in t)


def test_fresh_manifest_builds():
    man = build_free_core_manifest(REPO)
    assert man.get("merkle_root")
    assert man.get("count", 0) > 0


def test_check_seal_script_importable():
    # script should be runnable as module path
    import importlib.util
    p = REPO / "scripts" / "check_seal_freshness.py"
    spec = importlib.util.spec_from_file_location("check_seal_freshness", p)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    # writing to temp would reseal; just ensure main exists
    assert callable(mod.main)
