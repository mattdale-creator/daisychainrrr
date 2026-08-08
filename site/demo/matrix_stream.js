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
          nano_streams: st.nano_streams,
          utc: st.utc,
        },
        null,
        2
      );
    }
  } catch (e) {
    if (sealSnap) sealSnap.textContent = "status_snapshot.json not generated yet — run: python3 scripts/ttllm_status.py --write-site";
  }

  const nanoTipsLine = document.getElementById("nanoTipsLine");
  try {
    const r = await fetch("demo/nano_stream_tips.json", { cache: "no-store" });
    const tips = await r.json();
    if (nanoTipsLine) {
      const ok = tips.all_chain_ok ? "all chains ok" : "CHAIN BREAK";
      const bits = (tips.nanos || [])
        .map(function (n) {
          return n.name + " tip=" + ((n.tip || "").slice(0, 12)) + "…";
        })
        .join(" · ");
      nanoTipsLine.textContent = ok + " · " + (tips.nano_count || 0) + " nanos · " + bits;
    }
  } catch (e) {
    if (nanoTipsLine) nanoTipsLine.textContent = "nano tips missing — run: python3 scripts/publish_nano_stream_tips.py";
  }

  const publicProofLine = document.getElementById("publicProofLine");
  try {
    const r = await fetch("demo/public_proof.json", { cache: "no-store" });
    const p = await r.json();
    if (publicProofLine) {
      publicProofLine.textContent =
        (p.all_ok ? "all_ok true" : "all_ok false") +
        " · free_core " +
        (p.free_core_version || "?") +
        " · " +
        (p.utc || "");
    }
  } catch (e) {
    if (publicProofLine) publicProofLine.textContent = "public_proof missing — run: python3 scripts/public_proof.py";
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
