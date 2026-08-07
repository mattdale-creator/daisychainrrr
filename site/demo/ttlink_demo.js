(async function () {
  const stats = document.getElementById("stats");
  const results = document.getElementById("results");
  const input = document.getElementById("q");
  let docs = {};

  try {
    const res = await fetch("demo/ttlink_index.json");
    const data = await res.json();
    docs = data.docs || {};
    const n = Object.keys(docs).length;
    const bytes = Object.values(docs).reduce((a, d) => a + (d.bytes || 0), 0);
    stats.textContent = `Index loaded: ${n} docs · ${bytes} bytes · schema ${data.schema || "?"}`;
  } catch (e) {
    stats.textContent = "Failed to load index: " + e;
    return;
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  }

  function search() {
    const span = input.value;
    results.innerHTML = "";
    if (!span) {
      results.innerHTML = "<p class='mono'>Empty query.</p>";
      return;
    }
    const hits = [];
    for (const [docId, doc] of Object.entries(docs)) {
      const text = doc.text || "";
      let start = 0;
      while (true) {
        const i = text.indexOf(span, start);
        if (i < 0) break;
        const a = Math.max(0, i - 80);
        const b = Math.min(text.length, i + span.length + 80);
        hits.push({ docId, path: doc.path, start: i, end: i + span.length, context: text.slice(a, b), sha: doc.sha256, rel: i - a });
        start = i + 1;
        if (hits.length >= 20) break;
      }
      if (hits.length >= 20) break;
    }
    if (!hits.length) {
      results.innerHTML = "<p class='mono'>0 hits (exact match; try another span).</p>";
      return;
    }
    results.innerHTML = `<p class="mono">${hits.length} hit(s)</p>` + hits.map((h) => {
      const before = escapeHtml(h.context.slice(0, h.rel));
      const mid = escapeHtml(h.context.slice(h.rel, h.rel + span.length));
      const after = escapeHtml(h.context.slice(h.rel + span.length));
      return `<div class="hit"><div class="meta">${escapeHtml(h.path)} · [${h.start}:${h.end}] · sha256 ${h.sha.slice(0, 16)}…</div><div>${before}<mark>${mid}</mark>${after}</div></div>`;
    }).join("");
  }

  document.getElementById("run").onclick = search;
  document.getElementById("ex1").onclick = () => { input.value = "ttlink"; search(); };
  document.getElementById("ex2").onclick = () => { input.value = "OLMo"; search(); };
  document.getElementById("ex3").onclick = () => { input.value = "checkpoints"; search(); };
  input.addEventListener("keydown", (e) => { if (e.key === "Enter") search(); });
  search();
})();
