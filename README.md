# Monitor Polski w Markdown (od 2025 r.)

Teksty aktów z **Monitora Polskiego** od 2025 r. w Markdown i jako drzewo jednostek w JSON, z metadanymi
z API ELI Sejmu. Aktualizowane codziennie przez GitHub Actions.
*Texts of acts published in Monitor Polski (Poland's official gazette for non-statutory acts), 2025+,
as Markdown and as a JSON tree of units, converted from the official PDFs; updated daily.*

> **Nieoficjalne.** Teksty powstają przez automatyczną konwersję PDF-ów, więc mogą zawierać błędy.
> Wiążący jest PDF w Monitorze Polskim (link `source_pdf` w każdym pliku).

## Dlaczego

API ELI Sejmu (`api.sejm.gov.pl/eli`) podaje akty z Monitora Polskiego tylko jako PDF. Tekstu w HTML nie ma
dla żadnego aktu: 2025 – 0 z 1317, 2026 – 0 z 955 (sprawdzone 2026-09-29; wcześniejsze lata 2012–2024
też 0). Narzędzia, które budują na HTML, pomijają więc Monitor Polski w całości
(np. [legalize-pl](https://github.com/legalize-dev/legalize-pl) pobiera tylko Dziennik Ustaw).
Tutaj jest tekst tych aktów w formie, którą da się przeszukiwać, porównywać i przetwarzać.

W Monitorze Polskim są m.in. uchwały Sejmu i Senatu, zarządzenia, obwieszczenia i komunikaty organów
(np. wskaźniki i kwoty ogłaszane przez GUS i ministrów, wyniki wyborów) oraz postanowienia Prezydenta
(nadania orderów, nominacje). W 2025 r. (1317 aktów, według typu w API): postanowienia 566, uchwały 259,
obwieszczenia 239, komunikaty 137, zarządzenia 84, pozostałe 32.

## Stan

<!-- stats:start -->
Stan na 2026-09-29 20:37 UTC (liczone z `index.csv`, aktualizowane automatycznie).

| rok | aktów w indeksie | przekonwertowanych | błędów |
|---|---:|---:|---:|
| 2025 | 1317 | 1317 | 0 |
| 2026 | 955 | 955 | 0 |

Akty ze stronami bez warstwy tekstowej (skany, grafiki): 29, razem 525 z 10601 stron. Tekst z OCR (oznaczony) ma 467 z nich w 29 aktach; treści pozostałych brak.
Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): 36.

Rodzaje aktów: Postanowienie 851, Obwieszczenie 524, Uchwała 462, Komunikat 241, Zarządzenie 141, Ogłoszenie 22, Umowa międzynarodowa 14, Oświadczenie rządowe 14, Apel 2, Protokół 1.
Wersje konwertera: eli2md 0.6.2 (2272).
<!-- stats:end -->

## Zawartość

- `MP/<rok>/MP-<rok>-<pozycja>.md`: jeden akt. Front matter YAML z metadanymi ELI, potem tekst:
  `##### Art. N.` (albo `##### § N.`), akapity, `## Załącznik …`, przypisy `[^n]`.
  Ust., pkt i lit. zaczynają akapit. Indeksy jako znaki Unicode (`m²`).
- `MP/<rok>/MP-<rok>-<pozycja>.json`: ten sam akt jako drzewo jednostek (`art`, `par` (§), `ust`, `pkt`, `lit`,
  `tir`) z numerem, ścieżką (`par_2/ust_1/pkt_3`), tekstem i dziećmi. Opis:
  [README eli2md](https://github.com/PolskiAgentW/eli2md#json-drzewo-jednostek-od-053).
- `index.csv`: jeden wiersz na akt, także nieudany: `eli, year, pos, type, title, announcement_date,
  promulgation, change_date, pdf_sha256, pages, words, no_text_pages, image_pages, ocr_pages, status, error,
  converter, converted_at`.
- Cały zbiór w jednym pliku: [`monitor-polski-md.jsonl.gz`](https://github.com/PolskiAgentW/monitor-polski-md/releases/download/dane/monitor-polski-md.jsonl.gz)
  (JSON Lines, jeden akt w wierszu: kolumny `index.csv`, `meta` = front matter, `markdown` = tekst bez front
  matter, `tree` = drzewo z pliku `.json`). Odświeżany codziennie po aktualizacji (workflow „Eksport”).
  Przykład: `pandas.read_json("monitor-polski-md.jsonl.gz", lines=True)`.

Strony bez warstwy tekstowej (skany) czyta OCR (tesseract). Taki tekst jest oznaczony: przed stroną stoi notka
`> [Strona 5 PDF nie ma warstwy tekstowej. Tekst poniżej odczytał OCR …]`, a akapity OCR są cytatami blokowymi
(`> …`); w JSON to węzły `ocr`. OCR myli się częściej niż warstwa tekstowa, zwłaszcza w liczbach i tabelach.
Treści dużych obrazów (wzory, rysunki, mapy) tu nie ma; w tekście jest notka `> [Na stronie 7 PDF jest obraz …]`.
Tabele są spłaszczone do akapitów, wiersz po wierszu.

## Jak powstaje i jak dobre jest

Konwerter: [eli2md](https://github.com/PolskiAgentW/eli2md), ten sam co dla
[Dziennika Ustaw](https://github.com/PolskiAgentW/dziennik-ustaw-md). Jego jakość jest zmierzona na aktach
Dziennika Ustaw z 2024 r., które mają i PDF, i oficjalny HTML (wyniki w README eli2md).
**Dla Monitora Polskiego takiego wzorca nie ma** (brak HTML w API), więc jakość sprawdzam słabiej:

<!-- quality:start -->
- **Czy tekst nie ginie** (`eval/selfcheck.py` z eli2md, wszystkie 2272 akty 2025–2026, eli2md 0.6.2, 2026-09-29):
  porównuję słowa wyniku ze słowami warstwy tekstowej PDF (bez winiety i nagłówków stron, bez stron czytanych
  przez OCR). Mediana odsetka słów PDF obecnych w wyniku: **0.985**, odwrotnie (słowa wyniku obecne w PDF):
  **0.993**. Poniżej 0.95: 85 aktów, poniżej 0.8: 2. Z tych 85 aż 65 to krótkie akty (poniżej 400 słów), w których
  warstwa tekstowa PDF zawiera ukrytą kopię nagłówka wklejonego załącznika; konwerter ją celowo pomija
  (sprawdzone na MP/2025/613). Kolejności słów ani podziału na jednostki ta miara nie sprawdza.
- **Kontrola wzrokowa** (strona PDF obok wyniku), 8 aktów: MP/2025/418 (s. 34), 613 (s. 1–2), 241 (s. 6, OCR),
  MP/2026/580 oraz — na próbnej konwersji wersją rozwojową 0.6.2.dev0 — MP/2025/113, 148, 158: tekst
  i akapity zgodne z PDF. W OCR zdarzają się błędy znaków (w MP/2025/241 „m²” odczytane jako „m””). MP/2025/121:
  tekst pełny, ale w ciasno złożonej tabeli pozycje „2) … 5)” są doklejone do „1)”. Wybór częściowo losowy,
  częściowo celowy (długie akty, OCR, najniższe wyniki miary powyżej).
- **Znany błąd**: w wklejonych PDF-ach (załączniki) konwerter czasem gubi wąskie litery, np. „elekt omobinos ci”
  zamiast „elektromobilności” w MP/2025/1128 (odsetek słów 0.72). Poprawka w kolejnej wersji eli2md.
  Ilu aktów dotyczy, nie wiem dokładnie: ciągi pojedynczych liter są w 14 plikach, ale nie wszystkie to ten błąd.
- Drugi akt poniżej 0.8, MP/2025/541 (0.785): na s. 46–48 jest obrócona tabela z bardzo drobnym drukiem; w wyniku
  jest ok. 2/3 słów tych stron. Przyczyny jeszcze nie zbadałem.
- **Struktura** (art./§/ust./pkt/lit., drzewo JSON) jest zmierzona tylko na Dzienniku Ustaw 2024 (README eli2md).
  Obejrzane akty Monitora Polskiego mają podobny układ jak Dziennik Ustaw, ale struktury tu nie mierzyłem.
<!-- quality:end -->

Błędy konwersji zgłaszaj w Issues. Najlepiej podaj pozycję aktu i fragment.

Aktualizacja: codziennie o 04:53 UTC workflow `.github/workflows/update.yml` pobiera listę aktów
z API ELI. Konwertuje nowe akty oraz te, którym zmienił się `changeDate`, i commituje wynik.
Jeśli przez ponad 10 dni nie przybędzie żaden nowy akt, workflow kończy się błędem, żeby cicha awaria
była widoczna. Najdłuższa przerwa w ogłaszaniu aktów w Monitorze Polskim w latach 2025–2026 wyniosła 6 dni.

## Licencja

Akty normatywne i ich urzędowe projekty oraz urzędowe dokumenty i materiały nie są przedmiotem prawa
autorskiego (art. 4 pkt 1 i 2 ustawy o prawie autorskim i prawach pokrewnych). Pozostała zawartość
(indeks, skrypty): CC0 1.0.
