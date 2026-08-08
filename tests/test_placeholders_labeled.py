from pathlib import Path
import importlib.util

REPO = Path(__file__).resolve().parents[1]


def test_placeholder_labels():
    p = REPO / "scripts" / "check_placeholder_labels.py"
    spec = importlib.util.spec_from_file_location("check_ph", p)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    assert mod.main() == 0
