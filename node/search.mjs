// Get search results as JSON with the BestSERP API (Node.js 18+).
// Usage: BESTSERP_API_KEY=your_key node search.mjs "best running shoes"

const API_URL = "https://api.bestserp.com/search";

async function search(q, { gl = "us", hl = "en" } = {}) {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: {
      "X-API-KEY": process.env.BESTSERP_API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ q, gl, hl }),
  });
  if (!res.ok) throw new Error(`BestSERP request failed: HTTP ${res.status}`);
  return res.json();
}

const query = process.argv[2] ?? "best running shoes";
const data = await search(query);
for (const r of data.organic ?? []) {
  console.log(`${r.position}. ${r.title}\n   ${r.link}`);
}
