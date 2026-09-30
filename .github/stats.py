"""Rewrite the stats section of README.md from index.csv."""
import csv
import re
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path

rows = list(csv.DictReader(open("index.csv", encoding="utf-8")))
ok = [r for r in rows if r["status"] == "ok"]
years = sorted({r["year"] for r in rows})
lines = [f"Stan na {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC "
         f"(liczone z `index.csv`, aktualizowane automatycznie).", "",
         "| rok | aktów w indeksie | przekonwertowanych | błędów |", "|---|---:|---:|---:|"]
for y in years:
    ry = [r for r in rows if r["year"] == y]
    lines.append(f"| {y} | {len(ry)} | {sum(r['status'] == 'ok' for r in ry)} | "
                 f"{sum(r['status'] != 'ok' for r in ry)} |")
nt = [r for r in ok if int(r.get("no_text_pages") or 0) > 0]
ocr = [r for r in ok if int(r.get("ocr_pages") or 0) > 0]
lines += ["", f"Akty ze stronami bez warstwy tekstowej (skany, grafiki): {len(nt)}, "
              f"razem {sum(int(r['no_text_pages']) for r in nt)} z {sum(int(r['pages'] or 0) for r in ok)} stron. "
              f"Tekst z OCR (oznaczony) ma {sum(int(r['ocr_pages']) for r in ocr)} z nich w {len(ocr)} aktach; "
              f"treści pozostałych brak.",
          f"Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): "
          f"{sum(int(r.get('image_pages') or 0) > 0 for r in ok)}."]
types = Counter(r["type"] for r in ok)
lines += ["", "Rodzaje aktów: " + ", ".join(f"{t} {n}" for t, n in types.most_common()) + "."]
conv = Counter(r["converter"] for r in ok)
lines += ["Wersje konwertera: " + ", ".join(f"{c} ({n})" for c, n in conv.most_common()) + "."]
readme = Path("README.md").read_text(encoding="utf-8")
a, b = "<!-- stats:start -->", "<!-- stats:end -->"
i, j = readme.index(a) + len(a), readme.index(b)
Path("README.md").write_text(readme[:i] + "\n" + "\n".join(lines) + "\n" + readme[j:], encoding="utf-8")

# Consolidated texts (obwieszczenia "w sprawie ogłoszenia jednolitego tekstu ..."), newest per act. Monitor Polski
# has no HTML in the API for any act, so every consolidated text since 2012 is here.
tj = defaultdict(list)
for r in ok:
    m = re.search(r"jednolitego tekstu (.+?)\.?$", r["title"])
    if m:
        tj[re.sub(r"\s+[-–—]\s+", " – ", m.group(1).strip())].append(r)
for v in tj.values():
    v.sort(key=lambda r: (r["promulgation"], int(r["year"]), int(r["pos"])), reverse=True)


def link(r: dict) -> str:
    return f"[M.P. {r['year']} poz. {r['pos']}](MP/{r['year']}/MP-{r['year']}-{r['pos']}.md)"


def older(v: list) -> str:
    return ", ".join(link(r) for r in v[1:4]) + (f" i jeszcze {len(v) - 4}" if len(v) > 4 else "") or "–"


top = sorted(n for n in tj if re.match(r"uchwały (Sejmu|Senatu|Zgromadzenia Narodowego)", n))
tab = ["| Akt | Najnowszy tekst jednolity | Ogłoszony | Wcześniejsze |", "|---|---|---|---|"]
tab += [f"| {n[len('uchwały '):]} | {link(tj[n][0])} | {tj[n][0]['promulgation']} | {older(tj[n])} |" for n in top]
tab += ["", f"Wszystkie akty z tekstem jednolitym w tym zbiorze ({len(tj)}): [TEKSTY_JEDNOLITE.md](TEKSTY_JEDNOLITE.md)."]
readme = Path("README.md").read_text(encoding="utf-8")
a, b = "<!-- tj:start -->", "<!-- tj:end -->"
if a in readme:
    i, j = readme.index(a) + len(a), readme.index(b)
    Path("README.md").write_text(readme[:i] + "\n" + "\n".join(tab) + "\n" + readme[j:], encoding="utf-8")
full = ["# Teksty jednolite w Monitorze Polskim (od 2012 r.)", "",
        "Najnowszy tekst jednolity każdego aktu w tym zbiorze (z pliku `index.csv`, odświeżane automatycznie). "
        "Nazwa aktu pochodzi z tytułu obwieszczenia. Tekst jednolity podaje stan prawny na dzień wskazany "
        "w obwieszczeniu; zmian ogłoszonych później w nim nie ma. Teksty nieoficjalne, wiążący jest PDF.", ""]
kinds = sorted({n.split()[0] for n in tj}, key=lambda k: -sum(n.split()[0] == k for n in tj))
for kind in kinds:
    names = sorted((n for n in tj if n.split()[0] == kind), key=lambda n: n.lower())
    full += [f"## {kind[0].upper() + kind[1:]} ({len(names)})", "",
             "| Akt | Najnowszy | Ogłoszony | Wcześniejsze |", "|---|---|---|---|"]
    full += [f"| {n[len(kind) + 1:].replace('|', '/')} | {link(tj[n][0])} | {tj[n][0]['promulgation']} | {older(tj[n])} |"
             for n in names]
    full.append("")
Path("TEKSTY_JEDNOLITE.md").write_text("\n".join(full), encoding="utf-8")
