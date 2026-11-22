#!/usr/bin/env python3
"""Fetch the Netherlands Bach Society genre playlists from the YouTube Data API.

Usage: YT_API_KEY=... python3 scripts/fetch_playlists.py data/playlists.json

Writes {"fetched": "YYYY-MM-DD", "playlists": {playlist_id: [[video_id, seconds, title], ...]}}.
Only public, processed, embeddable videos with a known length are kept.
Exits non-zero (leaving the existing file untouched) if the API fails or the
catalogue shrinks suspiciously, so a bad week never empties the channels.
"""
import datetime, json, os, re, sys, urllib.parse, urllib.request

from channels import PLAYLISTS  # playlist ids, shared with build.py

API = "https://www.googleapis.com/youtube/v3/"
SUFFIX = re.compile(r"\s*\|\s*(Netherlands Bach Society|Nederlandse Bachvereniging).*$")
MIN_KEEP = 0.9  # refuse to publish if fewer than 90% of last week's recordings remain


def get(endpoint, **params):
    params["key"] = os.environ["YT_API_KEY"]
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def iso_seconds(d):
    m = re.fullmatch(r"P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?", d or "")
    if not m:
        return 0
    days, h, mins, s = (int(x or 0) for x in m.groups())
    return ((days * 24 + h) * 60 + mins) * 60 + s


def playlist_video_ids(pid):
    ids, token = [], None
    while True:
        params = dict(part="contentDetails", playlistId=pid, maxResults=50)
        if token:
            params["pageToken"] = token
        page = get("playlistItems", **params)
        ids += [it["contentDetails"]["videoId"] for it in page.get("items", [])]
        token = page.get("nextPageToken")
        if not token:
            return ids


def video_details(ids):
    out = {}
    for i in range(0, len(ids), 50):
        page = get("videos", part="snippet,contentDetails,status", id=",".join(ids[i:i + 50]))
        for v in page.get("items", []):
            st, sn = v.get("status", {}), v.get("snippet", {})
            secs = iso_seconds(v.get("contentDetails", {}).get("duration"))
            if (st.get("privacyStatus") == "public" and st.get("uploadStatus") == "processed"
                    and st.get("embeddable") and sn.get("liveBroadcastContent", "none") == "none" and secs > 0):
                out[v["id"]] = [v["id"], secs, SUFFIX.sub("", sn.get("title", "")).strip()]
    return out


def main(path):
    if not os.environ.get("YT_API_KEY"):
        sys.exit("YT_API_KEY is not set (add it under Settings → Secrets and variables → Actions)")
    order = {pid: playlist_video_ids(pid) for pid in PLAYLISTS.values()}
    every = list(dict.fromkeys(v for ids in order.values() for v in ids))
    details = video_details(every)
    playlists = {pid: [details[v] for v in ids if v in details] for pid, ids in order.items()}
    new_total = len({r[0] for rows in playlists.values() for r in rows})
    if new_total == 0:
        sys.exit("No videos returned; leaving the catalogue unchanged")
    if os.path.exists(path):
        old = json.load(open(path))
        old_total = len({r[0] for rows in old["playlists"].values() for r in rows})
        if new_total < MIN_KEEP * old_total:
            sys.exit(f"Catalogue shrank from {old_total} to {new_total} recordings; refusing to publish")
    data = {"fetched": datetime.date.today().isoformat(), "playlists": playlists}
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=0, separators=(",", ":"))
        f.write("\n")
    print(f"{new_total} recordings across {len(playlists)} playlists")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/playlists.json")
