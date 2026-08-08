# Dependency Register

## Public core / site / nano training

| Dependency | Category | Role | Disclosure notes |
|------------|----------|------|------------------|
| Apple M1 + macOS | hardware | nano training host | local |
| PyTorch 2.x | OSS library | training | BSD-style |
| Python 3 | runtime | tools + train | PSF |
| Project Gutenberg | data source | nano corpus | public domain US |
| Cloudflare Pages | infra | site hosting | ttllms project |
| Cloudflare Registrar/DNS | infra | domains | ttllms.com/org |
| GitHub | infra | source hosting | mattdale-creator/daisychainrrr |
| cryptography (PyCA) | OSS | Ed25519 optional | Apache-2.0 |
| free_core (this repo) | first-party | provenance/ttlink/stream | Apache-2.0 |

## Signing
Demo keys in `examples/keys/` are tutorial-only. Production HSM/threshold keys: not yet.
