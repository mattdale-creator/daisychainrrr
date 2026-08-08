# Hard technological & absolute-human gates (project-wide)

**Updated:** 2026-08-08  
**Purpose:** Inventory of gates that **cannot** be closed by writing more markdown, running more scripts, or agent simulation.  
**Complement:** Writable examples live under `docs/placeholders/` (each labeled **Written by Grok - Human checking required**).

---

## A. Hard technological gates (physics / platform / permission)

These fail even when the agent “knows exactly what to do.” Closing requires credentials, dashboard, or external systems outside agent control.

| ID | Gate | Why agent cannot close | Evidence / symptom | Human action |
|----|------|------------------------|--------------------|--------------|
| **T1** | **Cloudflare Zone DNS Edit for ttllms.org** | API returns auth/403 or token invalid; records not writable from this environment | `dig` → org has NS at Cloudflare but **no A/CNAME**; URL probe NXDOMAIN; historical 403 | Dashboard DNS: CNAME `@`/`www` → `ttllms.pages.dev` **or** issue PAT with Zone DNS Edit and run `ops/apply_dns_ttllms.sh` |
| **T2** | **Cloudflare R2 enable** | Account product not enabled; API error **10042** class until enable | Cannot create buckets via API | Dashboard → R2 → Enable → create `ttllm-public-releases` |
| **T3** | **Valid long-lived CF token with required scopes** | Current `CLOUDFLARE_API_TOKEN` verify can return **Invalid API Token** even when some Pages deploy still works via wrangler session | `tokens/verify` fail | Create/rotate token: Pages deploy, Zone DNS Edit (both zones), R2, optional Workers Routes |
| **T4** | **GitHub Actions workflow file push** | OAuth/PAT lacks **`workflow`** scope | Push rejected: *refusing to allow an OAuth App to create or update workflow* | PAT classic with `repo` + `workflow`; copy `docs/ci-templates/verify.yml` → `.github/workflows/` |
| **T5** | **Production HSM / offline multi-party key material** | No HSM device; no second party present; demo keys must not be production roots | `examples/keys/` tutorial only | Physical/ceremony path after entity; publish **public** key only |
| **T6** | **Government entity registration filing** | Agent cannot file with ASIC/Companies House/etc. or obtain ABN/EIN | No company number | Counsel + founder files formation |
| **T7** | **Bank / payment processor KYC** | Requires human identity verification and funds | No merchant account | Entity + KYC + bank |
| **T8** | **Real capital transfer** | Agent cannot move investor/bank money | No train cluster paid | Wire / raise / grant |
| **T9** | **Second biological custodian consent** | Recovery access requires a real person accepting legal/ops duty | ASSET_INVENTORY backup = unnamed | Name human, share recovery, Domain 1 log |
| **T10** | **Employment / contractor engagement of standing red team** | Hire is a human labor market act | No employee on payroll | Offer + signature + pay |
| **T11** | **Real customer signature + invoice payment** | Revenue requires counterparty | SKUs designed not sold | Sales + SOW + payment |

---

## B. Not hard gates (writable — now filled as Grok examples)

These were previously “human must write.” They are **example-complete** under `docs/placeholders/` with the Grok label. Human must **check and adopt**, not invent from zero.

| Topic | Placeholder path |
|-------|------------------|
| Full stewardship covenant | `docs/placeholders/legal/COVENANT_FULL_EXAMPLE.md` |
| Entity formation pack | `docs/placeholders/legal/ENTITY_FORMATION_PACK_EXAMPLE.md` |
| Safe harbor / report response | `docs/placeholders/legal/SAFE_HARBOR_AND_INTAKE_EXAMPLE.md` |
| Hosted-infra MSA | `docs/placeholders/commercial/MSA_HOSTED_INFRA_EXAMPLE.md` |
| DNS apply packet (exact records) | `docs/placeholders/ops/DNS_ORG_APPLY_PACKET.md` |
| R2 enable + first object | `docs/placeholders/ops/R2_ENABLE_AND_FIRST_BUCKET.md` |
| GitHub workflow scope packet | `docs/placeholders/ops/GITHUB_WORKFLOW_SCOPE_PACKET.md` |
| Key ceremony transcript | `docs/placeholders/security/KEY_CEREMONY_TRANSCRIPT_EXAMPLE.md` |
| Red-team SOW filled | `docs/placeholders/security/REDTEAM_SOW_FILLED_EXAMPLE.md` |
| CCO / Pliny-class role | `docs/placeholders/security/CCO_ROLE_DESCRIPTION.md` |
| Second custodian appointment | `docs/placeholders/org/SECOND_CUSTODIAN_APPOINTMENT.md` |
| Compensation bands | `docs/placeholders/org/COMPENSATION_BANDS_EXAMPLE.md` |
| Fundraise pitch + term sheet | `docs/placeholders/capital/*` |
| Scale budget filled | `docs/placeholders/capital/SCALE_BUDGET_FILLED_EXAMPLE.md` |
| First invoice / go-live | `docs/placeholders/commercial/FIRST_SKU_GO_LIVE_EXAMPLE.md` |
| Boundary annual attestation | `docs/placeholders/commercial/BOUNDARY_ANNUAL_ATTESTATION_EXAMPLE.md` |
| Cap table / funding history | `docs/placeholders/org/CAP_TABLE_AND_FUNDING_EXAMPLE.md` |
| Domain quarterly reports | `docs/placeholders/domains/` |
| 10-year financial model narrative | `docs/placeholders/capital/TEN_YEAR_FINANCIAL_MODEL_EXAMPLE.md` |

Index: `docs/placeholders/00-INDEX.md`

---

## C. Standing order (ethos)

1. Do not claim T1–T11 closed without evidence.  
2. Do not leave writable work blank when an example can be bone.  
3. Free public core never paywalled.  
4. Site (ttllms.com) updates as artefacts ship.  

**Contact:** md@0265.au  
**Vault SoT:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Founding ground truth:** `founding/conversation/TRANSCRIPT_ONLY.md`, `USER_PROMPTS.md`, Desktop archive `All Grok Build Conversations/LATEST`
