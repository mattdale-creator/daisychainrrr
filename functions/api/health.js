const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, OPTIONS", "Access-Control-Allow-Headers": "Content-Type" };
export async function onRequest(context) {
  if (context.request.method === "OPTIONS") return new Response(null, { headers: cors });
  return Response.json({
    ok: true,
    service: "ttllms-pages-functions",
    ethos: "down to the bone",
    free_core: true,
    paywall: false,
    utc: new Date().toISOString(),
  }, { headers: cors });
}
