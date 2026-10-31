#!/usr/bin/env python3
"""
counter.ink pipeline: social export -> filter -> select -> Markdown with site YAML.

Typical use (interactive; opens a selection page in your browser):

    python3 pipeline/pipeline.py --export ~/Downloads/facebook-XXXX

Other modes:
    --list        print candidates and exit
    --all         write every candidate without the selection page
    --dry-run     report what would be written, touch nothing

Only the standard library is used. Facebook export must be JSON format.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import mimetypes
import re
import shutil
import sys
import threading
import unicodedata
import webbrowser
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
POSTS_DIR = REPO / "content" / "blg" / "new"
IMAGES_DIR = REPO / "content" / "ci-img"
LEDGER = HERE / "seen.json"
URL_RE = re.compile(r"https?://\S+")


# --------------------------------------------------------------------------
# Normalized record: every ingester produces these, every emitter consumes them
# --------------------------------------------------------------------------
@dataclass
class Post:
    id: str
    platform: str
    ts: datetime
    text: str
    media: list = field(default_factory=list)  # list[Path]
    links: list = field(default_factory=list)  # list[str]


# --------------------------------------------------------------------------
# Ingest: Facebook JSON export
# --------------------------------------------------------------------------
def fix(s):
    """Facebook exports UTF-8 bytes as escaped Latin-1; undo that."""
    if not isinstance(s, str):
        return s
    try:
        return s.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s


def resolve_media(root: Path, uri: str):
    for base in (root, root.parent):
        p = base / uri
        if p.exists():
            return p
    return None


def localize(ts: int, tz):
    return datetime.fromtimestamp(ts, tz) if tz else datetime.fromtimestamp(ts).astimezone()


def ingest_facebook(export, tz):
    root = Path(export).expanduser().resolve()
    files = sorted(p for p in root.rglob("*.json") if re.match(r"your_posts.*\.json$", p.name))
    if not files:
        sys.exit(f"No your_posts*.json found under {root}.\n"
                 "Re-request the export with Format = JSON (not HTML).")
    posts, missing = {}, 0
    for f in files:
        with open(f, encoding="utf-8") as fh:
            data = json.load(fh)
        items = data if isinstance(data, list) else next((v for v in data.values() if isinstance(v, list)), [])
        for it in items:
            ts = it.get("timestamp")
            if not ts:
                continue
            texts, descs, media, links = [], [], [], []
            for d in it.get("data", []):
                if d.get("post"):
                    texts.append(fix(d["post"]))
            for att in it.get("attachments", []):
                for d in att.get("data", []):
                    m = d.get("media")
                    if m and m.get("uri"):
                        p = resolve_media(root, m["uri"])
                        if p:
                            media.append(p)
                        else:
                            missing += 1
                        if m.get("description"):
                            descs.append(fix(m["description"]))
                    ec = d.get("external_context")
                    if ec and ec.get("url"):
                        links.append(ec["url"])
            text = "\n\n".join(texts) or "\n\n".join(dict.fromkeys(descs))
            pid = "fb-" + hashlib.sha1(f"{ts}|{text[:80]}".encode()).hexdigest()[:12]
            posts[pid] = Post(pid, "facebook", localize(ts, tz), text.strip(), media, links)
    if missing:
        print(f"warning: {missing} media file(s) referenced but not found in the export", file=sys.stderr)
    return list(posts.values())


INGESTERS = {"facebook": ingest_facebook}  # add instagram / mastodon adapters here


# --------------------------------------------------------------------------
# Filter + ledger
# --------------------------------------------------------------------------
def body_len(text: str) -> int:
    return len(URL_RE.sub("", text).strip())


def load_ledger(path):
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save_ledger(path, ledger):
    Path(path).write_text(json.dumps(ledger, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def filter_posts(posts, since, until, min_chars, seen, include_seen):
    out = []
    for p in posts:
        d = p.ts.date()
        if since and d < since:
            continue
        if until and d > until:
            continue
        if body_len(p.text) < min_chars:
            continue
        if p.id in seen and not include_seen:
            continue
        out.append(p)
    return sorted(out, key=lambda p: p.ts)


def default_since(seen):
    """Day after the newest post in the FB archive folder. (Deliberately ignores the
    ledger: posts you skipped earlier should stay visible until you say otherwise.)"""
    dates = []
    for f in (REPO / "content" / "blg" / "old" / "social-media").rglob("*.md"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})-", f.name)
        if m:
            dates.append(m.group(1))
    return date.fromisoformat(max(dates)) + timedelta(days=1) if dates else None


def tag_vocab(limit=300):
    counts: dict[str, int] = {}
    for f in (REPO / "content" / "blg").rglob("*.md"):
        parts = f.read_text(encoding="utf-8", errors="ignore").split("---", 2)
        if len(parts) < 3:
            continue
        m = re.search(r"^tags:[ \t]*\n((?:[ \t]+-[^\n]*\n?)+)", parts[1], re.M)
        if not m:
            continue
        for line in m.group(1).splitlines():
            t = line.strip().lstrip("-").strip()
            if t:
                counts[t] = counts.get(t, 0) + 1
    return [t for t, _ in sorted(counts.items(), key=lambda kv: -kv[1])[:limit]]


# --------------------------------------------------------------------------
# Emit: Markdown + YAML header matching content/templates/new-note.md
# --------------------------------------------------------------------------
def clean(s) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def suggest_phrase(text: str, n: int = 7) -> str:
    words = URL_RE.sub("", text).split()[:n]
    return re.sub(r"[^\w\s’'-]", "", " ".join(words)).strip().lower()


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"['’]", "", s)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:70].strip("-") or "post"


def yq(v: str, force: bool = False) -> str:
    """Quote a YAML scalar only when needed (the site's headers are mostly bare)."""
    if v == "":
        return ""
    risky = (re.search(r":\s|\s#|:$|^[\-?:,\[\]{}#&*!|>'\"%@`]", v) or v != v.strip()
             or v.lower() in ("true", "false", "null", "yes", "no", "~"))
    if force or risky:
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return v


def build_header(title, description, extract, ts, has_media, tags) -> str:
    d, dt = ts.strftime("%Y-%m-%d"), ts.strftime("%Y-%m-%d %H:%M")
    lines = [
        "---",
        "yaml_begin: true",
        f"title: {yq(title)}".rstrip(),
        f"description: {yq(description)}".rstrip(),
        f"extract: {yq(extract, True)}".rstrip(),
        f"created: {dt}",
        f"updated: {dt}",
        "author: tb",
        f"images: {'true' if has_media else 'false'}",
        "order:",
        "enableToc: true",
        "permalink:",
        "aliases:",
        "publish: true",
        f"date: {d}",
        "tags:",
        *[f"  - {t}" for t in tags],
        "status:",
        'RSS: "true"',
        "yaml_end: true",
        "---",
    ]
    return "\n".join(lines) + "\n"


def body_text(text: str) -> str:
    text = text.replace("\r\n", "\n").strip()
    return re.sub(r"\n+", "\n\n", text)  # FB newline = line break; Markdown needs blank lines


def emit(selected, args):
    """selected: list of (Post, dict with title/description/extract/tags)."""
    posts_dir, images_dir = Path(args.posts_dir), Path(args.images_dir)
    ledger = load_ledger(args.ledger)
    report = []
    for post, sel in selected:
        d = post.ts.strftime("%Y-%m-%d")
        title = clean(sel.get("title")) or f"{d} {suggest_phrase(post.text)}".strip()
        slug = slugify(re.sub(r"^\d{4}-\d{2}-\d{2}[\s-]*", "", title))
        stem, n = f"{d}-{slug}", 2
        while (posts_dir / f"{stem}.md").exists():
            stem, n = f"{d}-{slug}-{n}", n + 1

        names = []
        for i, src in enumerate(post.media, 1):
            base = stem if len(post.media) == 1 else f"{stem}-{i}"
            name = f"{base}{src.suffix.lower()}"
            while (images_dir / name).exists():
                base += "-x"
                name = f"{base}{src.suffix.lower()}"
            if not args.dry_run:
                images_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, images_dir / name)
            names.append(name)

        tags = [clean(t) for t in re.split(r"[,\n]", sel.get("tags", "") or "") if clean(t)]
        header = build_header(title, clean(sel.get("description")), clean(sel.get("extract")),
                              post.ts, bool(names), tags)
        embeds = "\n".join(f"![[{n_}]]" for n_ in names)
        extra = [u for u in dict.fromkeys(post.links) if u not in post.text]
        parts = []
        if embeds and args.images_at == "top":
            parts.append(embeds)
        if post.text:
            parts.append(body_text(post.text))
        if extra:
            parts.append("\n".join(extra))
        if embeds and args.images_at == "bottom":
            parts.append(embeds)
        content = header + "\n\n".join(parts) + "\n"

        target = posts_dir / f"{stem}.md"
        if not args.dry_run:
            posts_dir.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            ledger[post.id] = {"date": d, "file": str(target.relative_to(REPO)) if REPO in target.parents else str(target),
                               "platform": post.platform}
        report.append(f"{'[dry] ' if args.dry_run else ''}{target.name}  ({len(names)} image(s))")
    if not args.dry_run:
        save_ledger(args.ledger, ledger)
    return "\n".join(report) or "nothing selected"


# --------------------------------------------------------------------------
# Selection UI: tiny local server, one page, one POST
# --------------------------------------------------------------------------
PAGE = """<!doctype html><meta charset="utf-8"><title>Select posts</title>
<style>
body{font:15px/1.45 system-ui,sans-serif;max-width:900px;margin:0 auto;padding:0 16px 80px;color:#222}
header{position:sticky;top:0;background:#fff;padding:10px 0;border-bottom:1px solid #ddd;z-index:5;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
input[type=search]{flex:1;min-width:160px;padding:6px}
.card{border:1px solid #ccc;border-radius:8px;margin:14px 0;padding:12px}
.card[hidden]{display:none}.card.on{border-color:#2a6;background:#f4fbf6}
.meta{color:#666;font-size:13px;margin-bottom:6px}
.txt{white-space:pre-wrap;max-height:260px;overflow:auto;border-left:3px solid #eee;padding-left:10px}
.imgs img{height:90px;margin:6px 6px 0 0;border-radius:4px}
.f{display:grid;grid-template-columns:90px 1fr;gap:4px 8px;margin-top:8px;font-size:13px}
.f input{padding:4px;width:100%;box-sizing:border-box}
button{padding:6px 12px}
</style>
<header>
<strong><span id=count>0</span> / __N__ selected</strong>
<input type=search id=q placeholder="filter text…">
<button id=selvis>select visible</button><button id=selnone>clear</button>
<button id=save disabled>Write files</button>
</header>
__CARDS__
<datalist id=tv>__TAGS__</datalist>
<script>
const cards=[...document.querySelectorAll('.card')];
const $=(c,s)=>c.querySelector(s);
function upd(){const n=cards.filter(c=>$(c,'.pick').checked).length;count.textContent=n;save.disabled=!n}
cards.forEach(c=>$(c,'.pick').addEventListener('change',()=>{c.classList.toggle('on',$(c,'.pick').checked);upd()}));
q.addEventListener('input',()=>{const t=q.value.toLowerCase();cards.forEach(c=>c.hidden=!!t&&!c.dataset.text.includes(t))});
selvis.onclick=()=>{cards.filter(c=>!c.hidden).forEach(c=>{$(c,'.pick').checked=true;c.classList.add('on')});upd()};
selnone.onclick=()=>{cards.forEach(c=>{$(c,'.pick').checked=false;c.classList.remove('on')});upd()};
save.onclick=async()=>{
  const sel=cards.filter(c=>$(c,'.pick').checked).map(c=>({id:c.dataset.id,title:$(c,'.title').value,
    description:$(c,'.desc').value,extract:$(c,'.ext').value,tags:$(c,'.tags').value}));
  save.disabled=true;
  const r=await fetch('/save',{method:'POST',body:JSON.stringify(sel)});const j=await r.json();
  document.body.innerHTML='<h3>Done</h3><pre>'+j.report.replace(/</g,'&lt;')+'</pre><p>You can close this tab.</p>';
};
</script>"""


def render_page(posts, vocab):
    cards = []
    for i, p in enumerate(posts):
        d = p.ts.strftime("%Y-%m-%d")
        imgs = "".join(f'<img src="/media/{i}/{j}" loading="lazy">' for j in range(len(p.media)))
        title = html.escape(f"{d} {suggest_phrase(p.text)}", quote=True)
        cards.append(f"""<div class=card data-id="{p.id}" data-text="{html.escape(p.text.lower(), quote=True)}">
<label><input type=checkbox class=pick> <strong>{d}</strong></label>
<div class=meta>{p.ts.strftime('%H:%M')} · {body_len(p.text)} chars · {len(p.media)} media · {len(p.links)} link(s)</div>
<div class=txt>{html.escape(p.text)}</div><div class=imgs>{imgs}</div>
<div class=f><label>title</label><input class=title value="{title}">
<label>description</label><input class=desc><label>extract</label><input class=ext>
<label>tags</label><input class=tags list=tv placeholder="comma-separated"></div></div>""")
    tags = "".join(f'<option value="{html.escape(t, quote=True)}">' for t in vocab)
    return PAGE.replace("__N__", str(len(posts))).replace("__CARDS__", "\n".join(cards)).replace("__TAGS__", tags)


def serve(posts, args):
    by_id = {p.id: p for p in posts}
    page = render_page(posts, tag_vocab()).encode("utf-8")

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, code, body, ctype):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path == "/":
                return self._send(200, page, "text/html; charset=utf-8")
            m = re.fullmatch(r"/media/(\d+)/(\d+)", self.path)
            if m:
                try:
                    f = posts[int(m[1])].media[int(m[2])]
                    return self._send(200, f.read_bytes(), mimetypes.guess_type(f.name)[0] or "application/octet-stream")
                except (IndexError, OSError):
                    pass
            self._send(404, b"not found", "text/plain")

        def do_POST(self):
            if self.path != "/save":
                return self._send(404, b"", "text/plain")
            sel = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"[]")
            chosen = [(by_id[s["id"]], s) for s in sel if s.get("id") in by_id]
            report = emit(chosen, args)
            self._send(200, json.dumps({"report": report}).encode(), "application/json")
            threading.Thread(target=srv.shutdown, daemon=True).start()

    port = args.port
    while True:
        try:
            srv = ThreadingHTTPServer(("127.0.0.1", port), H)
            break
        except OSError:
            port += 1
    url = f"http://127.0.0.1:{port}/"
    print(f"Selection page: {url}   (Ctrl-C to abort)")
    if not args.no_open:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("aborted; nothing written")
        return
    print("done.")


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--export", required=True, help="path to the unzipped platform export")
    ap.add_argument("--platform", default="facebook", choices=list(INGESTERS))
    ap.add_argument("--since", help="YYYY-MM-DD (default: day after newest already-ported post)")
    ap.add_argument("--until", help="YYYY-MM-DD")
    ap.add_argument("--min-chars", type=int, default=300, help="minimum length, URLs excluded (default 300)")
    ap.add_argument("--tz", help="IANA timezone for post times (default: this computer's)")
    ap.add_argument("--list", action="store_true", help="print candidates and exit")
    ap.add_argument("--all", action="store_true", help="write all candidates, no selection page")
    ap.add_argument("--include-seen", action="store_true", help="include posts already in the ledger")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--images-at", choices=["top", "bottom"], default="bottom")
    ap.add_argument("--posts-dir", default=str(POSTS_DIR))
    ap.add_argument("--images-dir", default=str(IMAGES_DIR))
    ap.add_argument("--ledger", default=str(LEDGER))
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-open", action="store_true")
    args = ap.parse_args()

    tz = ZoneInfo(args.tz) if args.tz else None
    seen = load_ledger(args.ledger)
    since = date.fromisoformat(args.since) if args.since else default_since(seen)
    until = date.fromisoformat(args.until) if args.until else None

    posts = INGESTERS[args.platform](args.export, tz)
    cands = filter_posts(posts, since, until, args.min_chars, seen, args.include_seen)
    print(f"{len(posts)} posts in export; {len(cands)} match "
          f"(since {since or 'start'}, until {until or 'now'}, >= {args.min_chars} chars)")

    if args.list:
        for p in cands:
            print(f"{p.ts:%Y-%m-%d}  {body_len(p.text):5d} chars  {len(p.media)} img  {p.text[:70]!r}")
        return
    if not cands:
        return
    if args.all:
        print(emit([(p, {}) for p in cands], args))
        return
    serve(cands, args)


if __name__ == "__main__":
    main()
