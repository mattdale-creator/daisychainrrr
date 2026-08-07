async function loadStream() {
  const chain = document.getElementById("chain");
  const box = document.getElementById("events");
  try {
    const res = await fetch("demo/public_log.json");
    const data = await res.json();
    chain.innerHTML = `schema <strong>${data.schema}</strong> · count <strong>${data.count}</strong> · tip <code>${(data.tip || "").slice(0, 24)}…</code> · <span class="status-ok">loaded</span>`;
    box.innerHTML = (data.events || []).map((e) => {
      return `<div class="card"><div class="mono">#${e.seq} · ${e.event_type} · ${e.timestamp_utc}</div>
        <pre>${JSON.stringify(e.payload, null, 2)}</pre>
        <div class="mono" style="color:var(--muted);font-size:.75rem">hash ${e.event_hash}<br/>prev ${e.prev_hash || "null"}</div></div>`;
    }).join("");
  } catch (err) {
    chain.textContent = "Failed: " + err;
  }
}
document.getElementById("reload").onclick = loadStream;
loadStream();
