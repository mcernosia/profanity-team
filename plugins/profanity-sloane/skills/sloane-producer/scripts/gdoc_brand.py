#!/usr/bin/env python3
"""
gdoc_brand.py: build the Profanity branding batch for a Google Doc.

Input:  a saved Docs read_doc result (JSON file). The wrapper {"content": {...}} is fine.
Output: JSON for update_doc: {"requests": [...], "writeControl": {"requiredRevisionId": ...}}

Usage:
    python3 gdoc_brand.py READ_DOC.json > batch.json

What it applies (brand-reference.md):
    - Azeret Mono over the whole body, near-black text (#1A1A1A)
    - The line right under the title (the date line) in gray (#808080)
    - Title and every heading: bold, keep-with-next, teal (#0ABAB5) rule underneath
    - Every table: thin gray (#808080) borders, teal header row, bold header text

Docs styles don't shift indexes, so one batch is safe. Read the doc again before
re-running: indexes go stale after any write.
"""
import json
import sys

TEAL = {"red": 0.039, "green": 0.729, "blue": 0.71}
BLACK = {"red": 0.102, "green": 0.102, "blue": 0.102}
GRAY = {"red": 0.502, "green": 0.502, "blue": 0.502}


def rgb(c):
    return {"color": {"rgbColor": c}}


def border(color, pt):
    return {"color": rgb(color), "width": {"magnitude": pt, "unit": "PT"}, "dashStyle": "SOLID"}


def main(path):
    with open(path) as f:
        data = json.load(f)
    doc = data.get("content", data)
    if "tabs" not in doc:
        sys.exit("No 'tabs' in the read_doc result. Pass the full read_doc JSON.")
    tab = doc["tabs"][0]
    tab_id = tab["tabProperties"]["tabId"]
    body = tab["documentTab"]["body"]["content"]
    body_end = body[-1]["endIndex"] - 1  # the final newline must stay

    def rng(start, end):
        return {"startIndex": start, "endIndex": end, "tabId": tab_id}

    reqs = []

    # 1. Body font + color, once, for everything (tables included).
    reqs.append({"updateTextStyle": {
        "range": rng(1, body_end),
        "textStyle": {"weightedFontFamily": {"fontFamily": "Azeret Mono"}, "foregroundColor": rgb(BLACK)},
        "fields": "weightedFontFamily,foregroundColor"}})

    # 2. Headings and the date line.
    seen_title = False
    date_done = False
    for el in body:
        p = el.get("paragraph")
        if not p:
            continue
        style = p.get("paragraphStyle", {}).get("namedStyleType", "")
        start, end = el["startIndex"], el["endIndex"]
        if style in ("TITLE", "HEADING_1") and not seen_title:
            seen_title = True
            rule = 2
        elif style.startswith("HEADING_") or style == "TITLE":
            rule = 1.5
        else:
            rule = None
            if seen_title and not date_done and style == "NORMAL_TEXT" and end - start > 1:
                date_done = True
                reqs.append({"updateTextStyle": {
                    "range": rng(start, end - 1),
                    "textStyle": {"foregroundColor": rgb(GRAY)},
                    "fields": "foregroundColor"}})
        if rule is not None:
            reqs.append({"updateParagraphStyle": {
                "range": rng(start, end),
                "paragraphStyle": {"keepWithNext": True, "borderBottom": {
                    **border(TEAL, rule), "padding": {"magnitude": 3 if rule < 2 else 4, "unit": "PT"}}},
                "fields": "keepWithNext,borderBottom"}})
            reqs.append({"updateTextStyle": {
                "range": rng(start, end - 1),
                "textStyle": {"bold": True},
                "fields": "bold"}})

    # 3. Tables.
    for el in body:
        t = el.get("table")
        if not t:
            continue
        rows, cols = t["rows"], t["columns"]
        loc = {"tableStartLocation": {"index": el["startIndex"], "tabId": tab_id},
               "rowIndex": 0, "columnIndex": 0}
        gray = border(GRAY, 0.75)
        reqs.append({"updateTableCellStyle": {
            "tableRange": {"tableCellLocation": loc, "rowSpan": rows, "columnSpan": cols},
            "tableCellStyle": {"borderTop": gray, "borderBottom": gray, "borderLeft": gray, "borderRight": gray},
            "fields": "borderTop,borderBottom,borderLeft,borderRight"}})
        reqs.append({"updateTableCellStyle": {
            "tableRange": {"tableCellLocation": loc, "rowSpan": 1, "columnSpan": cols},
            "tableCellStyle": {"backgroundColor": rgb(TEAL)},
            "fields": "backgroundColor"}})
        for cell in t["tableRows"][0]["tableCells"]:
            for ce in cell["content"]:
                if "paragraph" in ce and ce["endIndex"] - ce["startIndex"] > 1:
                    reqs.append({"updateTextStyle": {
                        "range": rng(ce["startIndex"], ce["endIndex"] - 1),
                        "textStyle": {"bold": True},
                        "fields": "bold"}})

    out = {"requests": reqs, "writeControl": {"requiredRevisionId": doc["revisionId"]}}
    json.dump(out, sys.stdout)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
