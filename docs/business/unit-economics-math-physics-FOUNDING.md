# $ math / physics / code (founding turn 13)

Here’s the hard math, physics, and code reality of running a TTLLM business with a free core and monetisation on the outside.

### 1. $ Math (order-of-magnitude)

**One-time / periodic cost to produce a serious TTLLM (32B-class, fully open)**  
- Pre-training a strong 32B on ~5.5–6T tokens currently lands in the **$2–4.5M** range in H100-equivalent compute at realistic 2026 rates (spot/reserved).  
- Full project (experiments + mid-training + post-training + multiple runs) realistically sits in the **$4–8M** band for a high-quality, reproducible release.  
- Smaller 7–13B versions are dramatically cheaper (low hundreds of thousands to low single-digit millions).

**Ongoing cost to keep the “down to the bone” layer public**  
- Training data + dense intermediate checkpoints + index: 50–150 TB is a realistic working set.  
- Object storage at current rates: roughly **$400–2,500 / month** depending on how much stays hot vs cold.  
- Low-latency ttlink serving (CPU + fast SSD for suffix-array / FM-index queries): a few thousand dollars per month for solid public performance.  
- Bandwidth if the public stream and downloads become popular: the variable that can spike.

**Break-even shape**  
The free core is a high fixed-cost, low marginal-cost public good.  
A handful of enterprise contracts (hosted inference with SLAs, private fine-tunes that still inherit full transparency guarantees, audit/compliance tooling, methodology consulting) at $50k–300k+ per year each can cover the ongoing burn and fund the next training run.  
The marketing advantage of radical transparency makes those contracts easier to close than for a normal closed model.

### 2. Physics / scaling constraints

- **Storage physics of true transparency**  
  Full training data for modern runs is multi-terabyte to low tens of terabytes compressed.  
  Exact-match indexing (the heart of a real ttlink system) currently costs ~7 bytes/token with classic suffix arrays, or ~0.44× corpus size with newer FM-index approaches. For a 6T-token corpus this is still tens of terabytes of index — perfectly feasible, but not free.

- **Checkpoint physics**  
  A 32B model is ~64 GB in BF16. Keeping hundreds of intermediate checkpoints “hot” gets expensive fast. Most must live in cold/archival storage and be pulled on demand. The public promise has to be honest about what is instantly available vs what is restorable.

- **Query physics**  
  Real-time “show me the source documents for this span” is CPU + disk IOPS bound, not GPU bound. It scales with good engineering (sharding the index, SSD, careful caching), not with more H100s.

### 3. Code / architecture reality

The minimal viable stack looks like this:

- **Training side**: Open training code + full data release + dense checkpointing (the OLMo-core / LLM360 pattern).  
- **ttlink engine**: Suffix-array or FM-index over the tokenised training data (infini-gram family or equivalent). This is what lets you go from any output span → exact matching documents in seconds.  
- **Public surface**:  
  - Continuous or on-demand stream of real data + linkages  
  - Web UI + API that turns the Matrix-style visual into a navigable surface (click a cascade → real documents appear)  
  - Optional richer enterprise layer on top (longer retention, private indexes, compliance exports, higher rate limits)

Everything commercial sits *outside* or *on top of* this free skeleton. The moment you have to hide data, checkpoints, or the linking mechanism to make money, the core premise collapses.

### Bottom line

The physics and the dollars both work at 32B scale today, provided the company is disciplined about what stays hot versus cold and treats the free public TTLLM as marketing + trust infrastructure rather than a direct profit centre.  

The expensive part is the initial (and periodic) training runs.  
The ongoing part is storage + indexing + serving the truth.  
The revenue sits in the reliability, compliance, and convenience layers that enterprises will pay for once they trust the skeleton is real.

That is the actual math.
