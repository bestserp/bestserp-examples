# BestSERP API examples

Code examples for [BestSERP](https://bestserp.com), a real-time SERP API: send a query, get the search results page back as clean JSON in seconds.

- 7 result types in one JSON format: web search, images, news, videos, shopping, places and maps
- Any country and language with `gl` and `hl`
- $0.50 per 1,000 searches, no subscription; failed searches are refunded
- 3,000 free searches to start, no credit card
- Serper-compatible: switch by changing the base URL and key

## Quick start

1. Create a free account and an API key at [bestserp.com](https://bestserp.com).
2. Put the key in an environment variable:

```bash
export BESTSERP_API_KEY="your_key_here"
```

3. Send a request:

```bash
curl -X POST 'https://api.bestserp.com/search' \
  -H "X-API-KEY: $BESTSERP_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"best running shoes","gl":"us","hl":"en"}'
```

## Examples

| Example | File | What it does |
| --- | --- | --- |
| cURL | [`curl/search.sh`](curl/search.sh) | Runs one search and prints position, title and link (needs `jq`) |
| Node.js | [`node/search.mjs`](node/search.mjs) | Runs one search with `fetch` (Node.js 18+) |
| Python | [`python/rank_tracker.py`](python/rank_tracker.py) | Finds where a domain ranks for a list of keywords and appends the result to `ranks.csv` |

Run the Python rank tracker:

```bash
cd python
pip install -r requirements.txt
python rank_tracker.py example.com "serp api" "google search api"
```

A step-by-step walkthrough of the rank tracker is on DEV: [Build a keyword rank tracker in Python in 30 lines](https://dev.to/bestserp/build-a-keyword-rank-tracker-in-python-in-30-lines-2ei0).

## Response shape

Every endpoint returns the same envelope. A trimmed web search response:

```json
{
  "searchParameters": { "q": "best running shoes", "gl": "us", "hl": "en", "type": "search" },
  "organic": [
    {
      "position": 1,
      "title": "Best running shoes: complete guide",
      "link": "https://guidehub.example/best-running-shoes",
      "snippet": "...",
      "domain": "guidehub.example"
    }
  ],
  "credits": 1
}
```

See [bestserp.com](https://bestserp.com) for the full list of endpoints and parameters.

## License

MIT
