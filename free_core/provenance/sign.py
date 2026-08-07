"""
Optional Ed25519 signing for manifests.

Requires: pip install 'ttllm-free-core[crypto]' or cryptography.
Signing keys are operational secrets; public keys and signatures are public.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

PathLike = Union[str, Path]


def _require_crypto():
    try:
        from cryptography.hazmat.primitives.asymmetric import ed25519
        from cryptography.hazmat.primitives import serialization
        return ed25519, serialization
    except ImportError as e:
        raise ImportError(
            "cryptography package required for signing. "
            "Install with: pip install cryptography"
        ) from e


def generate_keypair() -> Tuple[bytes, bytes]:
    """Return (private_pem, public_pem)."""
    ed25519, serialization = _require_crypto()
    private_key = ed25519.Ed25519PrivateKey.generate()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return private_pem, public_pem


def sign_manifest(manifest: dict, private_key_pem: bytes) -> dict:
    ed25519, serialization = _require_crypto()
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    payload = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    signature = private_key.sign(payload)
    return {
        "schema": "ttllm.signed_manifest.v1",
        "manifest": manifest,
        "signature_hex": signature.hex(),
        "algorithm": "ed25519",
    }


def verify_signed_manifest(signed: dict, public_key_pem: bytes) -> bool:
    ed25519, serialization = _require_crypto()
    public_key = serialization.load_pem_public_key(public_key_pem)
    manifest = signed["manifest"]
    payload = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    try:
        public_key.verify(bytes.fromhex(signed["signature_hex"]), payload)
        return True
    except Exception:
        return False


def write_keypair(dir_path: PathLike, name: str = "ttllm") -> Tuple[Path, Path]:
    d = Path(dir_path)
    d.mkdir(parents=True, exist_ok=True)
    priv, pub = generate_keypair()
    priv_p = d / f"{name}.private.pem"
    pub_p = d / f"{name}.public.pem"
    priv_p.write_bytes(priv)
    pub_p.write_bytes(pub)
    return priv_p, pub_p
