#!/usr/bin/env python3
"""Controlla riferimenti ed estratti negli output Markdown dell'agente."""

import argparse
import re
import sys
from pathlib import Path


REFERENCE = re.compile(
    r"\[([A-Za-z][A-Za-z0-9_-]*)\s*[–—-]\s*([^]\n–—]+?)"
    r"\s*[–—-]\s*([^]\n]+?)\]"
)
EXCERPT = re.compile(r"[ \t]*«([^»\n]*)»")
INSIGHT = re.compile(r"^### INSIGHT (I[0-9]+)\s*$")
HEADING = re.compile(r"^#{1,3}\s")


def read_utf8(path):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"Impossibile leggere {path}: {exc}") from exc


def validate_reference(source_dir, source_id, line_value, excerpt):
    if excerpt is None:
        return "non valida", "estratto mancante o non immediatamente accanto al riferimento"
    if not excerpt.strip() or len(excerpt.split()) > 15:
        return "non valida", "estratto vuoto o superiore a 15 parole"
    if not re.fullmatch(r"[1-9][0-9]*", line_value):
        return "non verificabile", "riferimento privo di numero di riga fisica"

    source = source_dir / f"{source_id}.md"
    if not source.is_file():
        return "non verificabile", f"fonte {source_id}.md assente"
    try:
        lines = read_utf8(source).splitlines()
    except ValueError as exc:
        return "non verificabile", str(exc)
    line_number = int(line_value)
    if line_number > len(lines):
        return "non valida", f"riga {line_number} fuori dall'intervallo della fonte"
    index = line_number - 1
    nearby = "\n".join(lines[max(0, index - 1):min(len(lines), index + 2)])
    if excerpt not in nearby:
        return "non valida", "estratto non presente sulla riga indicata o nelle righe adiacenti"
    return "valida", "riga ed estratto trovati"


def check(output, source_dir):
    citations = []
    insights = {}
    current_insight = None
    for output_line, text in enumerate(output.splitlines(), start=1):
        heading = INSIGHT.fullmatch(text)
        if heading:
            current_insight = heading.group(1)
            if current_insight in insights:
                raise ValueError(f"ID insight duplicato: {current_insight}")
            insights[current_insight] = []
        elif HEADING.match(text):
            current_insight = None

        for match in REFERENCE.finditer(text):
            source_id, profile, line_value = (part.strip() for part in match.groups())
            quote = EXCERPT.match(text, match.end())
            excerpt = quote.group(1) if quote else None
            status, reason = validate_reference(source_dir, source_id, line_value, excerpt)
            citation = (output_line, source_id, profile, line_value, status, reason)
            citations.append(citation)
            if current_insight is not None:
                insights[current_insight].append(citation)
    return citations, insights


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="output Markdown dell'agente, UTF-8")
    parser.add_argument("fonti", type=Path, help="cartella con un file UTF-8 ID.md per fonte")
    args = parser.parse_args(argv)
    if not args.fonti.is_dir():
        print(f"Errore: cartella delle fonti non accessibile: {args.fonti}", file=sys.stderr)
        return 2
    try:
        citations, insights = check(read_utf8(args.output), args.fonti)
    except ValueError as exc:
        print(f"Errore: {exc}", file=sys.stderr)
        return 2

    for status in ("valida", "non valida", "non verificabile"):
        items = [citation for citation in citations if citation[4] == status]
        print(f"Citazioni {status}: {len(items)}")
        for output_line, source_id, profile, line_value, _, reason in items:
            print(f"  output riga {output_line}: [{source_id} – {profile} – {line_value}] — {reason}")

    traceable = sum(
        bool(items) and all(citation[4] == "valida" for citation in items)
        for items in insights.values()
    )
    if insights:
        percentage = 100 * traceable / len(insights)
        print(f"Insight tracciabili: {traceable}/{len(insights)} ({percentage:.1f}%)")
    else:
        print("Insight tracciabili: non calcolabile (nessun insight dichiarato)")
    for insight_id, items in insights.items():
        if not items:
            print(f"  {insight_id}: nessuna citazione riconosciuta")
        elif any(citation[4] != "valida" for citation in items):
            print(f"  {insight_id}: una o più citazioni non sono valide")
    return int(any(citation[4] != "valida" for citation in citations)
               or any(not items for items in insights.values()))


if __name__ == "__main__":
    sys.exit(main())
