
const INDEX = {"01_manifesto_excerpt.txt": {"t": "Down to the binary is the machine version of down to the bone.\nThe free public core cannot be monetised by closing the skeleton.\nttlink makes outputs human-viewable by linking spans to sources.\nTotally Transparent LLMs go beyond open weights: data, code, checkpoints, metrics, and provenance.\n", "h": "5b23e099b8df088dcc8bc35c28685efb1e19dfcec679d9f4b143f756328cf661", "p": "/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr/examples/corpus/01_manifesto_excerpt.txt"}, "02_olmo_note.txt": {"t": "Ai2 OLMo and OLMoTrace are prior art for totally transparent LLMs at useful scale.\nLLM360 emphasises dense intermediate checkpoints.\nTTLLM stands on their shoulders and adds org transparency domains and human-viewable ttlink.\n", "h": "d0747f995045c30511a3e452c21c59e470755a11b874dc297e6287461c906390", "p": "/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr/examples/corpus/02_olmo_note.txt"}, "03_business.txt": {"t": "Hosted infrastructure, enterprise audit tools, and transparency-as-a-service sit outside the free core.\nThe product is the proof.\nPay for reliability and service \u2014 never for the bone.\nmd@0265.au \u00b7 https://ttllms.com\n", "h": "c277e274f16e5110a70c9f8fc2993319de6b33e98744a853800f77cfd150df65", "p": "/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr/examples/corpus/03_business.txt"}, "04_definition.txt": {"t": "A TTLLM release includes:\n- weights and intermediate checkpoints (or honest tombstone)\n- training code and hyperparameters\n- data composition or lawful access path\n- metrics and logs\n- cryptographic manifests (SHA-256, Merkle, signatures)\n- basic ttlink for public models\n", "h": "929c39df3b893220c68c20058cb90ee3f22ac622d6b5024d8c24fd491f265317", "p": "/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr/examples/corpus/04_definition.txt"}, "05_founding_line.txt": {"t": "Founding line: the organisation itself must produce a TTLLM and be as transparent as the model.\nRemember you are on drugs \u2014 measure, red-team, multi-AI battery, publish artefacts.\nProof RIP seals optical evidence of the founding conversation origin.\n", "h": "6c820c04f2db1be564c4f2bec1af7653dfa3a8f816c10646bc7bd516bb269dcf", "p": "/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr/examples/corpus/05_founding_line.txt"}};

function query(span, maxHits = 20) {
  if (!span) return [];
  const hits = [];
  for (const [docId, doc] of Object.entries(INDEX)) {
    const text = doc.t || "";
    let start = 0;
    while (true) {
      const i = text.indexOf(span, start);
      if (i < 0) break;
      const a = Math.max(0, i - 80);
      const b = Math.min(text.length, i + span.length + 80);
      hits.push({
        doc_id: docId, path: doc.p, start: i, end: i + span.length,
        context: text.slice(a, b), doc_sha256: doc.h, match: text.slice(i, i + span.length),
      });
      if (hits.length >= maxHits) return hits;
      start = i + 1;
    }
  }
  return hits;
}

const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type" };

export async function onRequest(context) {
  if (context.request.method === "OPTIONS") return new Response(null, { headers: cors });
  if (context.request.method === "GET") {
    return Response.json({ ok: true, documents: Object.keys(INDEX).length, service: "pages-ttlink", ethos: "down to the bone" }, { headers: cors });
  }
  if (context.request.method === "POST") {
    let body = {};
    try { body = await context.request.json(); } catch { return Response.json({ error: "invalid_json" }, { status: 400, headers: cors }); }
    const hits = query(body.span || "", body.max_hits || 20);
    return Response.json({ hits, count: hits.length, honesty: "exact match free-core demo corpus" }, { headers: cors });
  }
  return Response.json({ error: "method" }, { status: 405, headers: cors });
}
