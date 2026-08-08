async function loadNanoTips() {
  const tipsEl = document.getElementById("nano-tips");
  if (!tipsEl) return;
  try {
    const res = await fetch("demo/nano_stream_tips.json");
    const data = await res.json();
    const badge = data.all_chain_ok
      ? `<span class="status-ok">all chains ok</span>`
      : `<span class="status-bad">chain break</span>`;
    const rows = (data.nanos || [])
      .map((n) => {
        const ok = n.chain_ok ? "ok" : "FAIL";
        const tip = (n.tip || "").slice(0, 20);
        const href = n.site_log || "#";
        return `<tr>
          <td class="mono">${n.name}</td>
          <td>${ok}</td>
          <td>${n.count ?? "—"}</td>
          <td class="mono" title="${n.tip || ""}">${tip}…</td>
          <td>${n.last_event_type || "—"}</td>
          <td><a href="${href}">log</a></td>
        </tr>`;
      })
      .join("");
    tipsEl.innerHTML = `
      <p class="mono">schema <strong>${data.schema}</strong> · nanos <strong>${data.nano_count}</strong> · ${badge}</p>
      <p class="tagline" style="margin-top:.5rem">${data.ethos || ""}</p>
      <div style="overflow-x:auto">
        <table class="mono" style="width:100%;font-size:.85rem;border-collapse:collapse">
          <thead><tr>
            <th align="left">release</th><th align="left">chain</th><th align="left">events</th>
            <th align="left">tip</th><th align="left">last</th><th align="left">file</th>
          </tr></thead>
          <tbody>${rows}</tbody>
        </table>
      </div>
      <p style="margin-top:.75rem">Source: <a href="demo/nano_stream_tips.json">demo/nano_stream_tips.json</a>
        · publish: <code>python3 scripts/publish_nano_stream_tips.py</code></p>`;
  } catch (err) {
    tipsEl.textContent = "Nano tips failed: " + err;
  }
}

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
document.getElementById("reload").onclick = () => {
  loadNanoTips();
  loadStream();
};
loadNanoTips();
loadStream();
