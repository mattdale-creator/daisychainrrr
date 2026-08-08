"""Ensure commercial BOUNDARY still forbids core-closing language."""
from pathlib import Path

def test_boundary_has_prohibited_opacity():
    text = Path("commercial/BOUNDARY.md").read_text()
    assert "Prohibited opacity" in text or "prohibited" in text.lower()
    assert "paywall" in text.lower() or "Paywall" in text
    assert "free public core" in text.lower() or "Free public core" in text

def test_isolation_runbook_exists():
    p = Path("commercial/ISOLATION_RUNBOOK.md")
    assert p.is_file()
    t = p.read_text()
    assert "Separate" in t or "separate" in t
    assert "signing keys" in t.lower() or "Signing keys" in t
