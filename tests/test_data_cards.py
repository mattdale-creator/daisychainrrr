"""Domain 3 DATA_CARD machine checks."""
from pathlib import Path
import sys
import importlib.util

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))


def _load():
    p = REPO / "scripts" / "check_data_cards.py"
    spec = importlib.util.spec_from_file_location("check_data_cards", p)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


def test_data_cards_structure():
    mod = _load()
    cards = mod.find_cards(REPO)
    assert cards, "expected at least one DATA_CARD"
    for c in cards:
        errs = mod.check_card(c, verify_files=False)
        assert not errs, errs


def test_data_cards_cli_ok():
    mod = _load()
    assert mod.main([]) == 0
