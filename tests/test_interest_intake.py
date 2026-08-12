"""Interest intake classifier + domain scorecard."""
from pathlib import Path
import json
import subprocess
import sys

from free_core.business.interest_intake import (
    DEMO_MESSAGES,
    PATH_COMMERCIAL_INTEREST,
    PATH_FUND_SCALE,
    PATH_GENERAL,
    PATH_REFUSE_CLOSE_CORE,
    PATH_VERIFY,
    classify_interest,
    demo_corpus_ok,
)
from free_core.org.domain_scorecard import build_domain_scorecard

REPO = Path(__file__).resolve().parents[1]


def test_demo_corpus_paths():
    assert demo_corpus_ok() is True
    for text, expected in DEMO_MESSAGES:
        assert classify_interest(text).path == expected


def test_refuse_beats_commercial_words():
    # exclusive free-core still refuse even if "buy" appears
    v = classify_interest(
        "We want to buy exclusive free-core weights and paywall verification"
    )
    assert v.path == PATH_REFUSE_CLOSE_CORE
    assert v.selling is False
    assert v.severity == "refuse"


def test_paths_named():
    assert classify_interest("enterprise ttlink and hosted SLA").path == PATH_COMMERCIAL_INTEREST
    assert classify_interest("invest in 32B train at scale").path == PATH_FUND_SCALE
    assert classify_interest("verify merkle public_proof").path == PATH_VERIFY
    assert classify_interest("hello there").path == PATH_GENERAL


def test_interest_intake_script_demo():
    p = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "interest_intake.py"), "--demo", "--write-site"],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0, p.stdout + p.stderr
    out = REPO / "site" / "demo" / "interest_intake_demo.json"
    assert out.is_file()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["pre_revenue"] is True
    assert data["selling"] is False
    assert data["demo_corpus_ok"] is True
    assert data["count"] == 5


def test_domain_scorecard_ten_rows():
    card = build_domain_scorecard(REPO)
    assert card["schema"] == "ttllm.domain_scorecard.v1"
    assert len(card["domains"]) == 10
    # Domain 8 should be pre-revenue MET given commercial bone
    d8 = next(d for d in card["domains"] if d["number"] == 8)
    assert d8["status"] == "MET-pre-revenue"
    assert card["artefact_md_count"] >= 50
