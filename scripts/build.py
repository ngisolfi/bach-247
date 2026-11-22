#!/usr/bin/env python3
"""Build index.html from template.html and the fetched catalogue.

Usage: python3 scripts/build.py data/playlists.json template.html index.html
"""
import datetime, json, sys

from channels import CHANNELS, EXTRA, PLAYLISTS


def main(data_path, template_path, out_path):
    data = json.load(open(data_path))
    lists = data["playlists"]
    vids, idx = [], {}
    for pid in PLAYLISTS.values():  # fixed playlist order keeps the catalogue stable between runs
        for vid, secs, title in lists.get(pid, []):
            if vid not in idx and secs > 0:
                idx[vid] = len(vids)
                vids.append([vid, secs, title])

    def items(keys):
        out = []
        for k in keys:
            for vid, _, _ in lists.get(PLAYLISTS[k], []):
                if vid in idx and idx[vid] not in out:
                    out.append(idx[vid])
            for vid in EXTRA.get(k, []):
                if vid in idx and idx[vid] not in out:
                    out.append(idx[vid])
        return out

    channels = []
    for key, name, keys in CHANNELS:
        it = list(range(len(vids))) if keys == "*" else items(keys)
        if it:
            channels.append({"key": key, "name": name, "items": it})
        print(f"{name}: {len(it)} recordings, {sum(vids[i][1] for i in it) / 3600:.1f} h")

    d = datetime.date.fromisoformat(data["fetched"])
    snapshot = f"{d.day} {d:%B %Y}"
    html = open(template_path).read()
    html = html.replace("__VIDEOS__", json.dumps(vids, ensure_ascii=False, separators=(",", ":")))
    html = html.replace("__CHANNELS__", json.dumps(channels, ensure_ascii=False, separators=(",", ":")))
    html = html.replace("__SNAPSHOT__", snapshot)
    open(out_path, "w").write(html)


if __name__ == "__main__":
    main(*sys.argv[1:4])
