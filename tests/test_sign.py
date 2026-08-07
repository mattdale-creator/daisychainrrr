import pytest
from free_core.provenance.manifest import build_merkle_manifest
from free_core.provenance.sign import generate_keypair, sign_manifest, verify_signed_manifest

def test_sign_roundtrip(tmp_path):
    try:
        priv, pub = generate_keypair()
    except ImportError:
        pytest.skip("cryptography not installed")
    f = tmp_path / "a.txt"
    f.write_text("bone")
    m = build_merkle_manifest([f], base=tmp_path)
    signed = sign_manifest(m, priv)
    assert verify_signed_manifest(signed, pub) is True
    signed["signature_hex"] = "00" * 64
    assert verify_signed_manifest(signed, pub) is False
