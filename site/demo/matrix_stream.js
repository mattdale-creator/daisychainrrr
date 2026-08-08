/* Real stream + API + seal snapshot — no aesthetic without data */
(async function () {
  const streamTip = document.getElementById("streamTip");
  const streamEvents = document.getElementById("streamEvents");
  const sealSnap = document.getElementById("sealSnap");
  const apiOut = document.getElementById("apiOut");
  const apiPing = document.getElementById("apiPing");

  try {
    const r = await fetch("demo/public_log.json", { cache: "no-store" });
    const log = await r.json();
    if (streamTip) {
      streamTip.textContent =
        "events=" + (log.count || (log.events || []).length) +
        " tip=" + (log.tip || "").slice(0, 16) + "…";
    }
    if (streamEvents) {
      const ul = document.createElement("ul");
      ul.className = "clean";
      (log.events || []).slice(-8).forEach(function (e) {
        const li = document.createElement("li");
        li.innerHTML =
          "<code>" +
          (e.event_type || "?") +
          "</code> · seq " +
          e.seq +
          " · " +
          (e.timestamp_utc || "");
        ul.appendChild(li);
      });
      streamEvents.appendChild(ul);
    }
  } catch (e) {
    if (streamTip) streamTip.textContent = "stream load failed (local file missing?)";
  }

  try {
    const r = await fetch("demo/status_snapshot.json", { cache: "no-store" });
    const st = await r.json();
    if (sealSnap) {
      sealSnap.textContent = JSON.stringify(
        {
          free_core_version: st.free_core_version,
          seal: st.seal,
          ethos: st.ethos,
          utc: st.utc,
        },
        null,
        2
      );
    }
  } catch (e) {
    if (sealSnap) sealSnap.textContent = "status_snapshot.json not generated yet — run: python3 scripts/ttllm_status.py --write-site";
  }

  const inclSnap = document.getElementById("inclSnap");
  try {
    const r = await fetch("demo/inclusion_proof_sample.json", { cache: "no-store" });
    const j = await r.json();
    if (inclSnap) {
      inclSnap.textContent = JSON.stringify(
        {
          verified: j.verified,
          path: j.path,
          merkle_root: j.merkle_root,
          leaf_count: j.leaf_count,
          leaf_hash: j.proof && j.proof.leaf_hash,
          proof_steps: j.proof && j.proof.proof && j.proof.proof.length,
          recipe: j.recipe,
        },
        null,
        2
      );
    }
  } catch (e) {
    if (inclSnap) inclSnap.textContent = "inclusion_proof_sample.json missing — run: python3 scripts/demo_inclusion_proof.py";
  }

  if (apiPing && apiOut) {
    apiPing.addEventListener("click", async function () {
      apiOut.textContent = "…";
      try {
        const r = await fetch("/api/ttlink/", { cache: "no-store" });
        const j = await r.json();
        apiOut.textContent = JSON.stringify(j, null, 2);
      } catch (err) {
        apiOut.textContent = String(err);
      }
    });
  }
})();
