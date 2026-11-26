"""Convert kb/01-coverage-tracker.md into tracker.csv for the coverage dashboard
(https://claude.ai/artifact/9FU4XgSiCzDjeZMfwnr4Au).
Usage: python3 md_to_csv.py <tracker.md> <out.csv>
"""
import csv, re, sys

STATUSES = ["needs-1.0-check", "partial", "done", "retired", "todo"]

def parse(md):
    rows, area = [], None
    for line in md.splitlines():
        h = re.match(r"^## (.+?)(?: — .*)?$", line)
        if h:
            area = h.group(1).strip()
            continue
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Topic"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        topic, doc, raw = cells[0], cells[1], cells[2]
        batch = cells[3] if len(cells) > 3 else ""
        status = next((s for s in STATUSES if raw.lower().startswith(s)), "todo")
        note = raw[len(status):].strip(" —-()") if raw.lower().startswith(status) else raw
        m = re.match(r"(\d+)", batch)
        rows.append({
            "area": area, "topic": topic, "doc": "kb/" + doc, "status": status,
            "batch": int(m.group(1)) if m else "", "note": note,
        })
    return rows

def updated(md):
    m = re.search(r"Last updated:\s*(\S+)", md)
    return m.group(1) if m else ""

if __name__ == "__main__":
    md = open(sys.argv[1], encoding="utf-8").read()
    rows = parse(md)
    with open(sys.argv[2], "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["area", "topic", "doc", "status", "batch", "note"])
        w.writeheader(); w.writerows(rows)
    print(len(rows), "rows; tracker last updated", updated(md))
