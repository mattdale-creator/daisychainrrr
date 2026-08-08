# Stream event catalog (normative)

Generated from `free_core.stream.catalog.EVENT_TYPES`.

| event_type | description | nano | scale | required_payload |
|------------|-------------|------|-------|------------------|
| `decision` | Material Domain 1 decision referenced publicly | optional | required_when_material | decision_id, summary |
| `data_prepared` | Training data mixture prepared and carded | required | required | card |
| `training_started` | Training run began | required | required | hyper |
| `loss_metric` | Periodic or final loss/metric sample | recommended | required | — |
| `checkpoint_saved` | Public intermediate checkpoint written | optional | required_on_interval | path |
| `training_finished` | Training run completed | recommended | required | — |
| `release` | Public release claim with merkle root | required | required | name, version |
| `seal` | Merkle seal of free core or release tree | recommended | required | manifest |
| `ttlink_index_sealed` | ttlink index sealed for public corpus | required | required | docs |
| `site_deploy` | Public site deploy | optional | optional | url |
| `architect` | Architecture tree / handbook milestone | optional | optional | tree |
| `incident_opened` | High/Critical incident opened (public-safe) | on_incident | on_incident | incident_id, severity |
| `claim_tombstoned` | Public claim tombstoned due to integrity or honesty | on_incident | on_incident | claim, reason |
| `incident_mitigated` | Incident mitigation applied | on_incident | on_incident | incident_id |
| `incident_closed` | Incident closed with residual risk note | on_incident | on_incident | incident_id, residual |
| `incident_drill` | Synthetic tabletop drill (not a production incident) | optional | optional | scenario |
| `boundary_attestation` | Domain 8 boundary attestation published | optional | annual_when_selling | period |
| `redteam_finding` | Significant red-team finding registered | on_finding | on_finding | finding_id, severity |

## Nano minimum set

`data_prepared`, `training_started`, `release`, `ttlink_index_sealed`

## Scale minimum set

`data_prepared`, `training_started`, `loss_metric`, `training_finished`, `release`, `seal`, `ttlink_index_sealed`

*Soft tissue forbidden: inventing events without artefacts.*
