"""Inclusion-proof demo script produces verified sample."""
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parents[1]


def test_demo_inclusion_proof_readme():
    r = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "demo_inclusion_proof.py")],
        cwd=str(REPO),
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr + r.stdout
    sample = REPO / "site" / "demo" / "inclusion_proof_sample.json"
    assert sample.is_file()
    import json

    data = json.loads(sample.read_text(encoding="utf-8"))
    assert data["verified"] is True
    assert data["path"] == "README.md"
    assert data["merkle_root"]
