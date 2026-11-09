#!/usr/bin/env python3
"""
Add the front Firefox tab (title + URL) to content/recent.md as a new
microblog entry, just beneath the pinned note.

    ./add_recent.py              # grab front Firefox tab (macOS), insert entry
    ./add_recent.py -n           # dry run: show the result, write nothing
    ./add_recent.py --url URL --title TITLE   # skip Firefox, supply by hand

Format produced:   ***YYYY-MM-DD:*** [Title](URL)

Layout rules (matching the existing file):
  - same day as the newest entry  -> new entry goes on top of that day's
    group, separated from the next entry by one blank line
  - new day -> new entry, blank line, `***`, blank line, then the previous day
  - new month -> `### YYYY-MM` goes above the pinned note and the old month
    header moves below the new entry (likewise `## YYYY` if the
    year changed)
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
import time
from pathlib import Path

RECENT = Path(__file__).resolve().parent / "content" / "recent.md"
PINNED_MARKER = "2026-11-05-a-bill-to-defeat-supreme-court-corruption"
URL_RE = re.compile(r"^[a-z][a-z0-9+.-]*://\S+$", re.I)
ENTRY_RE = re.compile(r"^\*\*\*(\d{4}-\d{2}-\d{2}):\*\*\*")
MONTH_RE = re.compile(r"^### (\d{4}-\d{2})\s*$")
YEAR_RE = re.compile(r"^## (\d{4})\s*$")


# ---------- Firefox ----------

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def osa(script):
    r = run(["osascript", "-e", script])
    if r.returncode != 0:
        sys.exit(f"osascript failed: {r.stderr.strip()}\n"
                 "(Terminal/your launcher needs Accessibility permission "
                 "in System Settings > Privacy & Security.)")
    return r.stdout.strip()


def wait_for_modifiers_released(timeout=4.0):
    """The hotkey that launched us (e.g. cmd-ctrl-w) may still be held down;
    any keystrokes we send meanwhile would pick up those modifiers."""
    import ctypes
    cg = ctypes.CDLL("/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics")
    cg.CGEventSourceFlagsState.restype = ctypes.c_uint64
    cg.CGEventSourceFlagsState.argtypes = [ctypes.c_int32]
    mask = 0x20000 | 0x40000 | 0x80000 | 0x100000   # shift, ctrl, option, cmd
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not (cg.CGEventSourceFlagsState(1) & mask):
            time.sleep(0.1)
            return
        time.sleep(0.05)


def copy_address_bar(tries=3):
    import uuid
    for _ in range(tries):
        # pbcopy with empty input doesn't reliably clear the clipboard, so
        # plant a unique marker and wait for it to be replaced by the URL.
        marker = f"__add_recent_probe_{uuid.uuid4().hex}__"
        run(["pbcopy"], input=marker)
        osa('tell application "System Events"\n'
            '  keystroke "l" using command down\n'
            '  delay 0.25\n'
            '  keystroke "c" using command down\n'
            'end tell')
        end = time.time() + 1.5
        while time.time() < end:
            got = run(["pbpaste"]).stdout.strip()
            if URL_RE.match(got):     # ignore stale/foreign clipboard contents
                return got
            time.sleep(0.05)
    return ""


def firefox_is_frontmost():
    return osa('tell application "System Events" to get frontmost of process "firefox"') == "true"


def front_title():
    return osa('tell application "System Events" to tell process "firefox" '
               'to get name of front window')


def front_firefox_tab():
    """Return (title, url) of the front tab of Firefox's front window."""
    wait_for_modifiers_released()
    osa('tell application "Firefox" to activate')
    deadline = time.time() + 4
    while time.time() < deadline and not firefox_is_frontmost():
        time.sleep(0.1)
    if not firefox_is_frontmost():
        sys.exit("Couldn't bring Firefox to the front.")
    time.sleep(0.3)
    saved = run(["pbpaste"]).stdout          # preserve text clipboard
    try:
        for _ in range(3):
            title = front_title()
            url = copy_address_bar()
            if url and front_title() == title:   # same tab before and after
                break
            url = ""
    finally:
        osa('tell application "System Events" to key code 53')  # Esc: back to page
        run(["pbcopy"], input=saved)
    if not url:
        sys.exit("Didn't get a URL from the address bar.")
    return title, url


def clean_title(title):
    title = re.sub(r"\s+[—–-]\s+Mozilla Firefox(\s+Private Browsing)?\s*$", "", title)
    title = " ".join(title.split())
    return title.replace("[", r"\[").replace("]", r"\]")


def clean_url(url):
    return url.replace("(", "%28").replace(")", "%29").replace(" ", "%20")


# ---------- recent.md ----------

def insert_entry(text, entry_line, today):
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = text.splitlines()

    # end of the pinned callout block
    start = next((i for i, l in enumerate(lines)
                  if l.startswith(">") and PINNED_MARKER in l), None)
    if start is None:
        sys.exit("Couldn't find the pinned note in recent.md.")
    end = start
    while end + 1 < len(lines) and lines[end + 1].startswith(">"):
        end += 1

    p = end + 1
    while p < len(lines) and lines[p].strip() == "":
        p += 1                                # first content line after pin

    m = ENTRY_RE.match(lines[p]) if p < len(lines) else None
    same_day = bool(m and m.group(1) == today)

    if same_day:
        new = lines[:end + 1] + [""] + [entry_line, ""] + lines[p:]
    else:
        # swallow an existing separator so we don't double it
        if p < len(lines) and lines[p].strip() == "***":
            p += 1
            while p < len(lines) and lines[p].strip() == "":
                p += 1
        prefix, new_hdrs, old_hdrs = lines[:start], [], []
        # month header currently above the pin (and its year header, if adjacent)
        h = next((i for i in range(start - 1, -1, -1) if MONTH_RE.match(lines[i])), None)
        cur_month = MONTH_RE.match(lines[h]).group(1) if h is not None else None
        if cur_month != today[:7] and h is not None:
            y = next((i for i in range(h - 1, -1, -1) if YEAR_RE.match(lines[i])), None)
            cur_year = YEAR_RE.match(lines[y]).group(1) if y is not None else None
            cut = h
            if cur_year != today[:4] and y is not None and all(
                    l.strip() == "" for l in lines[y + 1:h]):
                cut = y
                new_hdrs += [f"## {today[:4]}", ""]
                old_hdrs += [lines[y], ""]
            new_hdrs += [f"### {today[:7]}", ""]
            old_hdrs += [lines[h], ""]
            prefix = lines[:cut]
        else:
            prefix = lines[:start]
            # headers stay where they are; keep everything above the pin
        if new_hdrs:
            new = prefix + new_hdrs + lines[start:end + 1] + [""] \
                  + [entry_line, "", "***", ""] + old_hdrs + lines[p:]
        else:
            new = lines[:end + 1] + [""] + [entry_line, "", "***", ""] + lines[p:]
    return nl.join(new) + (nl if text.endswith(("\n", "\r\n")) else "")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-n", "--dry-run", action="store_true")
    ap.add_argument("--url")
    ap.add_argument("--title")
    ap.add_argument("--file", default=str(RECENT), help="markdown file to edit")
    ap.add_argument("--date", help="override today (YYYY-MM-DD), for testing")
    a = ap.parse_args()

    if a.url and a.title:
        title, url = a.title, a.url
    else:
        title, url = front_firefox_tab()
    today = a.date or dt.date.today().isoformat()
    entry = f"***{today}:*** [{clean_title(title)}]({clean_url(url)})"

    path = Path(a.file)
    old = path.read_text(encoding="utf-8")
    new = insert_entry(old, entry, today)

    if a.dry_run:
        print(entry)
        print("--- preview (top of file) ---")
        print("\n".join(new.splitlines()[22:40])[:3000])
        return
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(new, encoding="utf-8")
    tmp.replace(path)
    print("Added:", entry)


if __name__ == "__main__":
    main()
