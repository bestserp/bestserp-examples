"""Track where a domain ranks for a list of keywords with the BestSERP API.

Usage:
    export BESTSERP_API_KEY=your_key
    python rank_tracker.py example.com "serp api" "google search api"

Each run appends one row per keyword to ranks.csv: date, keyword, position, url.
"""
import csv
import datetime
import os
import sys

import requests

API_URL = "https://api.bestserp.com/search"


def search(q, gl="us", hl="en"):
    r = requests.post(
        API_URL,
        headers={
            "X-API-KEY": os.environ["BESTSERP_API_KEY"],
            "Content-Type": "application/json",
        },
        json={"q": q, "gl": gl, "hl": hl},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def rank_of(domain, q, gl="us"):
    for item in search(q, gl=gl).get("organic", []):
        if domain in item["link"]:
            return item["position"], item["link"]
    return None, None


def track(domain, keywords, path="ranks.csv"):
    today = datetime.date.today().isoformat()
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        for kw in keywords:
            pos, url = rank_of(domain, kw)
            print(f"{kw!r}: {pos or 'not in top 10'} {url or ''}")
            w.writerow([today, kw, pos or "", url or ""])


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    track(sys.argv[1], sys.argv[2:])
