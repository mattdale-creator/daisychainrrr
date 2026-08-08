from free_core.ttlink.index import TtlinkIndex
from free_core.security.canary import inject_canary, check_canary

def test_canary_detects_presence():
    idx = TtlinkIndex()
    inject_canary(idx, "test-secret-1")
    r = check_canary(idx, "test-secret-1")
    assert r["ok"] is True

def test_canary_missing():
    idx = TtlinkIndex()
    r = check_canary(idx, "test-secret-1")
    assert r["ok"] is False
