# Public Stream

The stream is the mechanism left open — not a cinematic representation.

## Event types

- `data_shard` — new public shard released  
- `checkpoint` — intermediate or final weights published  
- `ttlink_hit` — optional public query telemetry (privacy-preserving)  
- `decision` — material organisational decision affecting the core  
- `loss_metric` — training metrics snapshots  
- `release` — versioned package release  

Schema: `free_core/stream/schema.py` (`ttllm.stream_event.v1`).
