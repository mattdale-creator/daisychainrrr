from free_core.provenance.manifest import build_merkle_manifest, verify_manifest, write_manifest, load_manifest
from free_core.provenance.hashing import sha256_bytes

def test_sha256_empty():
    assert sha256_bytes(b"") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

def test_merkle_stable(tmp_path):
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("down to the bone")
    b.write_text("ttlink")
    m1 = build_merkle_manifest([a, b], base=tmp_path)
    m2 = build_merkle_manifest([b, a], base=tmp_path)
    assert m1["merkle_root"] == m2["merkle_root"]
    write_manifest(m1, tmp_path / "m.json")
    assert verify_manifest(load_manifest(tmp_path / "m.json"), tmp_path)["ok"] is True

def test_tamper_detected(tmp_path):
    a = tmp_path / "a.txt"
    a.write_text("original")
    m = build_merkle_manifest([a], base=tmp_path)
    a.write_text("tampered")
    assert verify_manifest(m, tmp_path)["ok"] is False
