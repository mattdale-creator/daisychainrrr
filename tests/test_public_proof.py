"""Unpaid public proof script (free_core 0.6.3)."""
from pathlib import Path
import json
import subprocess
import sys

REPO = Path(__file__).resolve().parents[1]


def test_public_proof_script_ok():
    p = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "public_proof.py")],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0, p.stdout + p.stderr
    out = REPO / "site" / "demo" / "public_proof.json"
    assert out.is_file()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["schema"] == "ttllm.public_proof.v1"
    assert data["all_ok"] is True
    assert data["direction"]["on_track"] is True
    assert data["ethos"]["free_public_core_never_paywalled"] is True
    assert data["checks"]["free_core_seal_green"] is True
    assert data["checks"]["nano_streams_all_chain_ok"] is True


def test_public_proof_excluded_from_seal():
    from free_core.provenance.seal_targets import SEAL_EXCLUDE_NAMES

    assert "public_proof.json" in SEAL_EXCLUDE_NAMES
    assert "status_snapshot.json" in SEAL_EXCLUDE_NAMES
