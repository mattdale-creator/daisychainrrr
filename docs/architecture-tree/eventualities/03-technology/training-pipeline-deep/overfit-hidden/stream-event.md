# 03-technology/training-pipeline-deep/overfit-hidden/stream-event.md · stream-event

**Path:** `eventualities/03-technology/training-pipeline-deep/overfit-hidden/stream-event.md`  
**Updated:** 2026-08-08  
**Leaf type:** stream-event — what public stream event to emit

## Purpose
What public stream event to emit for: **component** · failure · phase before public release or claim · actor project lead / founder.

## When to emit
Emit a public stream event if free-core verification surfaces or public claims were affected.

## Event shape
Use `free_core.stream` / `ttllm-stream`:
- `event_type`: one of `incident`, `tombstone`, `reseal`, `domain_gap`, `supply_chain`
- `payload`: summary, path `03-technology/training-pipeline-deep/overfit-hidden/stream-event.md`, severity, link to register entry (no secrets)
- Keep hash chain intact (`ttllm-stream verify`)

## Example
```bash
python3 -m free_core.stream.cli append models/ttllm-nano/stream/public_log.json \
  --type tombstone --payload '{"path":"03-technology/training-pipeline-deep/overfit-hidden/stream-event.md","note":"gap disclosed"}'
python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
```


## Artefacts / tools
- Paths: `see parent README`
- Registers: registers/incidents/ or registers/decisions/ as appropriate
- Verify suite: `scripts/oneshot_verify_all.py`, `scripts/redteam_nano_harness.py`

## Done when
- [x] Written procedure exists (this file)
- [ ] Owner has executed once (drill or real)
- [ ] Linked failure mode cannot recur without detection

## Related
Parent node README; `docs/specs/`; `commercial/BOUNDARY.md`; `STATUS_HONEST.md`
