# Public stream architecture

**Updated:** 2026-08-07

## Purpose

Append-only public events for seals, releases, decisions, evals — hash-chained so tip proves history.

## Reference implementation

```bash
ttllm-stream build-demo-log -o examples/stream/public_log.json
ttllm-stream verify examples/stream/public_log.json
```

Browser: https://ttllms.com/stream.html

Schema: `ttllm.stream_log.v1` with per-event `event_hash` and `prev_hash`.
