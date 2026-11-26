"""Shared schema constants + parsers for the exiles-codex KB (used by convert.py and lint.py)."""
import re

VOL = {'stable', 'may-change', 'volatile', 'retired'}
CONF = {'confirmed', 'single-source', 'inferred', 'conflict'}
VERS = ['1.0', '0.5.5.9', '0.5.5', '0.5.x', '0.5.0', '0.5']
STATUS = {'done', 'partial', 'todo', 'needs-1.0-check', 'retired'}

DATE_RE = re.compile(r'20\d\d-\d\d-\d\d')
URL_RE = re.compile(r'https?://[^\s)\]>|]+')
MDLINK_RE = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
LINK_RE = re.compile(r'\[\[([^\]|#]+)')
PRICE_RE = re.compile(r'\b\d[\d.,]*\s*(div|divine|ex|exalt|chaos)s?\b', re.I)
INF_NOREASON_RE = re.compile(r'\[INFERRED\]\s*[:\-—–]?\s*$', re.M)
META_RE = re.compile(r'^@ (.*)$')
POE2DB_RE = re.compile(r'https?://(?:www\.)?poe2db\.tw/us/([^\s)\]#?]+)')


def norm_version(v):
    s = (v or '').strip().lower()
    if not s:
        return None
    m = re.search(r'(1\.0|0\.5\.5\.9|0\.5\.5|0\.5\.x|0\.5\.0|0\.5)', s)
    if m and s.find(m.group(1)) <= 25:  # "game data 0.5.5.9 (...)" -> 0.5.5.9
        return m.group(1)
    if re.match(r'0\.[0-4]', s) or 'early access' in s:
        return '0.5.x'  # older-era claim still described as current-in-0.5; raw text kept
    return None


def norm_enum(v, allowed):
    s = (v or '').strip().lower()
    if not s:
        return None
    if s.startswith('[inferred'):
        return 'inferred' if 'inferred' in allowed else None
    w = re.split(r'[\s(;,—–:]', s)[0].strip('*.').strip()
    if w in allowed:
        return w
    if w in ('partly', 'partial') and 'single-source' in allowed:
        return 'single-source'
    return None


def parse_meta(line):
    m = META_RE.match(line)
    if not m:
        return None
    out = {}
    for tok in m.group(1).split():
        if '=' in tok:
            k, v = tok.split('=', 1)
            out[k] = v
    return out


def slug(h):
    return re.sub(r'[^a-z0-9]+', '-', h.lower()).strip('-')[:60]
