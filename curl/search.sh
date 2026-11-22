#!/usr/bin/env bash
# Get search results as JSON with the BestSERP API.
# Usage: BESTSERP_API_KEY=your_key ./search.sh "best running shoes"
# Needs curl and jq.
set -euo pipefail

query="${1:-best running shoes}"
body=$(jq -n --arg q "$query" '{q: $q, gl: "us", hl: "en"}')

curl -sS -X POST 'https://api.bestserp.com/search' \
  -H "X-API-KEY: ${BESTSERP_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d "$body" | jq '.organic[] | {position, title, link}'
