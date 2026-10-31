#!/usr/bin/env python3
"""Build a synthetic Facebook JSON export (with FB's Latin-1 mojibake) for testing."""
import json, sys
from datetime import datetime, timezone
from pathlib import Path

out = Path(sys.argv[1])
posts_dir = out / "your_facebook_activity" / "posts"
media_dir = posts_dir / "media"
media_dir.mkdir(parents=True, exist_ok=True)

def moji(s):  # what Facebook does to every string
    return s.encode("utf-8").decode("latin-1")

def ts(y, m, d, h=12):
    return int(datetime(y, m, d, h, tzinfo=timezone.utc).timestamp())

for n in ("a.jpg", "b.JPEG", "c.png"):
    (media_dir / n).write_bytes(b"\xff\xd8\xff\xe0fakeimage-" + n.encode())

LONG = ("Here’s a longer post about adjuncts: it has “curly quotes”, an em—dash, and emoji 🎉.\n"
        "A second line with a #hashtag and a link https://example.com/story that shouldn’t count toward length.\n"
        "Third paragraph. " + "Lorem ipsum dolor sit amet. " * 14)

items = [
    {"timestamp": ts(2025, 1, 15), "data": [{"post": moji(LONG)}]},                        # long, no media
    {"timestamp": ts(2025, 2, 3), "data": [{"post": moji("too short")}]},                   # short -> filtered
    {"timestamp": ts(2025, 3, 9), "data": [{"post": moji("Look: " + "word " * 80)}],        # 2 images + link
     "attachments": [{"data": [
         {"media": {"uri": "your_facebook_activity/posts/media/a.jpg"}},
         {"media": {"uri": "your_facebook_activity/posts/media/b.JPEG"}},
         {"external_context": {"url": "https://example.org/article"}}]}]},
    {"timestamp": ts(2025, 4, 1), "data": [],                                               # link-only share
     "attachments": [{"data": [{"external_context": {"url": "https://example.org/only-a-link"}}]}]},
    {"timestamp": ts(2025, 5, 20), "data": [],                                              # photo; text only in description
     "attachments": [{"data": [{"media": {"uri": "your_facebook_activity/posts/media/c.png",
                                           "description": moji("Caption: " + "pic " * 90)}}]}]},
    {"timestamp": ts(2024, 6, 1), "data": [{"post": moji("Old and long. " * 40)}]},         # before --since
    {"timestamp": ts(2025, 6, 2), "data": [{"post": moji("Title: with a colon. " + "x " * 160)}]},  # YAML-risky title
    {"timestamp": ts(2025, 6, 2, 15), "data": [{"post": moji("Title: with a colon. " + "x " * 160)}]},  # same-day slug collision
]
(posts_dir / "your_posts__check_ins__photos_and_videos_1.json").write_text(
    json.dumps(items, ensure_ascii=True), encoding="utf-8")
print("fake export at", out)
