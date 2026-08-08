"""Commercial SKU catalog + commercial_status (business bone)."""
from pathlib import Path
import json
import subprocess
import sys

from free_core.business.sku_catalog import catalog_ok, load_sku_catalog

REPO = Path(__file__).resolve().parents[1]


def test_sku_catalog_six_designed():
    cat = load_sku_catalog(REPO)
    assert cat["schema"] == "ttllm.sku_catalog.v1"
    assert cat["sku_count"] == 6
    assert cat["pre_revenue"] is True
    assert cat["integrity"]["ok"] is True
    assert catalog_ok(REPO) is True
    for s in cat["skus"]:
        assert s["designed_not_sold"] is True
        assert s["live_claim"] is False
        assert s["free_core_unaffected"] is True


def test_commercial_status_script():
    p = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "commercial_status.py")],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0, p.stdout + p.stderr
    out = REPO / "site" / "demo" / "commercial_status.json"
    assert out.is_file()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["all_ok"] is True
    assert data["selling"] is False
    assert data["pre_revenue"] is True
    assert data["sku_catalog"]["sku_count"] == 6


def test_commercial_status_excluded_from_seal():
    from free_core.provenance.seal_targets import SEAL_EXCLUDE_NAMES

    assert "commercial_status.json" in SEAL_EXCLUDE_NAMES
