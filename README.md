# Monitor Polski w Markdown (od 2012 r.)

Teksty aktów z **Monitora Polskiego** od 2012 r. w Markdown i jako drzewo jednostek w JSON, z metadanymi
z API ELI Sejmu. Aktualizowane codziennie przez GitHub Actions.
*Texts of acts published in Monitor Polski (Poland's official gazette for non-statutory acts), 2012+,
as Markdown and as a JSON tree of units, converted from the official PDFs; updated daily.*

> **Nieoficjalne.** Teksty powstają przez automatyczną konwersję PDF-ów, więc mogą zawierać błędy.
> Wiążący jest PDF w Monitorze Polskim (link `source_pdf` w każdym pliku).

<!-- zbiory:start -->
**Wszystkie zbiory** (ten sam format plików, konwerter [eli2md](https://github.com/PolskiAgentW/eli2md)). Akty, które API ELI
podaje w HTML (np. większość Dziennika Ustaw 2012–2024), nie są tu powielane.

| lata | Dziennik Ustaw | Monitor Polski |
|---|---|---|
| od 2012 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-md): od 2025 r. wszystkie, wcześniej 98 aktów bez HTML; codziennie | [GitHub](https://github.com/PolskiAgentW/monitor-polski-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-md): wszystkie z PDF (API nie ma HTML); codziennie |
| 2000–2011 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-2000-2011-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-2000-2011-md): akty bez HTML w API | [GitHub](https://github.com/PolskiAgentW/monitor-polski-2000-2011-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-2000-2011-md): wszystkie z PDF |
| 1990–1999 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-1990-1999-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-1990-1999-md): akty bez HTML w API (OCR skanów) | brak |
| 1918–1989 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-1918-1989-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-1918-1989-md): akty bez HTML w API (OCR skanów; pomiar jakości w README) | brak |

Kolumny są we wszystkich zbiorach te same, więc lata można wczytać razem (nadal bez aktów, które API ELI podaje w HTML):

```python
from datasets import load_dataset

du = load_dataset("parquet", split="train", data_files=[
    "hf://datasets/PolskiAgentW/dziennik-ustaw-1918-1989-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-1990-1999-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-2000-2011-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-md/data/*.parquet",
])  # 58 761 aktów (2026-10-09); Monitor Polski: monitor-polski-2000-2011-md + monitor-polski-md
```
<!-- zbiory:end -->

## Dlaczego

API ELI Sejmu (`api.sejm.gov.pl/eli`) podaje akty z Monitora Polskiego tylko jako PDF. Tekstu w HTML nie ma
dla żadnego aktu: 2025 – 0 z 1317, 2026 – 0 z 955, 2012–2024 – 0 z 15 885 (sprawdzone 2026-09-29). Narzędzia, które budują na HTML, pomijają więc Monitor Polski w całości
(np. [legalize-pl](https://github.com/legalize-dev/legalize-pl) pobiera tylko Dziennik Ustaw).
Tutaj jest tekst tych aktów w formie, którą da się przeszukiwać, porównywać i przetwarzać.
Lata 2000–2011 (11 977 aktów) są w osobnym repozytorium [monitor-polski-2000-2011-md](https://github.com/PolskiAgentW/monitor-polski-2000-2011-md).

W Monitorze Polskim są m.in. uchwały Sejmu i Senatu, zarządzenia, obwieszczenia i komunikaty organów
(np. wskaźniki i kwoty ogłaszane przez GUS i ministrów, wyniki wyborów) oraz postanowienia Prezydenta
(nadania orderów, nominacje). W 2025 r. (1317 aktów, według typu w API): postanowienia 566, uchwały 259,
obwieszczenia 239, komunikaty 137, zarządzenia 84, pozostałe 32.

## Stan

<!-- stats:start -->
Stan na 2026-10-10 05:09 UTC (liczone z `index.csv`, aktualizowane automatycznie).

| rok | aktów w indeksie | przekonwertowanych | błędów |
|---|---:|---:|---:|
| 2012 | 1024 | 1024 | 0 |
| 2013 | 1041 | 1041 | 0 |
| 2014 | 1226 | 1226 | 0 |
| 2015 | 1307 | 1307 | 0 |
| 2016 | 1257 | 1257 | 0 |
| 2017 | 1224 | 1224 | 0 |
| 2018 | 1291 | 1291 | 0 |
| 2019 | 1207 | 1207 | 0 |
| 2020 | 1217 | 1217 | 0 |
| 2021 | 1206 | 1206 | 0 |
| 2022 | 1291 | 1291 | 0 |
| 2023 | 1482 | 1482 | 0 |
| 2024 | 1112 | 1112 | 0 |
| 2025 | 1317 | 1317 | 0 |
| 2026 | 984 | 984 | 0 |

Akty ze stronami bez warstwy tekstowej (skany, grafiki): 426, razem 14297 z 98755 stron. Tekst z OCR (oznaczony) ma 12667 z nich w 415 aktach; treści pozostałych brak.
Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): 565.

Rodzaje aktów: Postanowienie 7144, Obwieszczenie 4031, Uchwała 2751, Komunikat 2060, Zarządzenie 1271, Oświadczenie rządowe 329, Umowa międzynarodowa 309, Ogłoszenie 241, Orzeczenie 19, Porozumienie 9, Protokół 8, Apel 4, Stanowisko 3, Rezolucja 3, Informacja 1, Traktat 1, Opinia 1, Oświadczenie 1.
Wersje konwertera: eli2md 0.6.25 (9817), eli2md 0.6.25.2 (6594), eli2md 0.6.25.1 (1775).
<!-- stats:end -->

## Teksty jednolite

Monitor Polski nie ma w API HTML-a dla żadnego aktu, więc teksty jednolite z Monitora Polskiego też są tylko w PDF,
np. Regulaminu Sejmu, Regulaminu Senatu i statutów urzędów. Tutaj jest najnowszy tekst jednolity każdego aktu.
Tabela jest odświeżana razem ze zbiorem. Tekst jednolity podaje stan prawny na dzień wskazany w obwieszczeniu.
Zmian ogłoszonych później w nim nie ma.

<!-- tj:start -->
| Akt | Najnowszy tekst jednolity | Ogłoszony | Wcześniejsze |
|---|---|---|---|
| Sejmu Rzeczypospolitej Polskiej – Regulamin Sejmu Rzeczypospolitej Polskiej | [M.P. 2026 poz. 573](MP/2026/MP-2026-573.md) | 2026-06-09 | [M.P. 2022 poz. 990](MP/2022/MP-2022-990.md), [M.P. 2021 poz. 483](MP/2021/MP-2021-483.md), [M.P. 2019 poz. 1028](MP/2019/MP-2019-1028.md) i jeszcze 1 |
| Senatu Rzeczypospolitej Polskiej – Regulamin Senatu | [M.P. 2025 poz. 1251](MP/2025/MP-2025-1251.md) | 2025-12-15 | [M.P. 2024 poz. 10](MP/2024/MP-2024-10.md), [M.P. 2018 poz. 846](MP/2018/MP-2018-846.md), [M.P. 2017 poz. 827](MP/2017/MP-2017-827.md) i jeszcze 3 |

Wszystkie akty z tekstem jednolitym w tym zbiorze (131): [TEKSTY_JEDNOLITE.md](TEKSTY_JEDNOLITE.md).
<!-- tj:end -->

## Zawartość

- `MP/<rok>/MP-<rok>-<pozycja>.md`: jeden akt. Front matter YAML z metadanymi ELI, potem tekst:
  `##### Art. N.` (albo `##### § N.`), akapity, `## Załącznik …`, przypisy `[^n]`.
  Ust., pkt i lit. zaczynają akapit. Indeksy jako znaki Unicode (`m²`).
- `MP/<rok>/MP-<rok>-<pozycja>.json`: ten sam akt jako drzewo jednostek (`art`, `par` (§), `ust`, `pkt`, `lit`,
  `tir`) z numerem, ścieżką (`par_2/ust_1/pkt_3`), tekstem i dziećmi. Opis:
  [README eli2md](https://github.com/PolskiAgentW/eli2md#json-drzewo-jednostek-od-053).
- `index.csv`: jeden wiersz na akt, także nieudany: `eli, year, pos, type, title, announcement_date,
  promulgation, change_date, pdf_sha256, pages, words, no_text_pages, image_pages, ocr_pages, image_ocr_pages,
  status, error, converter, converted_at`. `image_ocr_pages` (od eli2md 0.6.4): liczba stron, na których OCR
  odczytał obraz tekstu na stronie z warstwą tekstową (s. 1 umów międzynarodowych; 11 aktów).
- Cały zbiór w jednym pliku: [`monitor-polski-md.jsonl.gz`](https://github.com/PolskiAgentW/monitor-polski-md/releases/download/dane/monitor-polski-md.jsonl.gz)
  (JSON Lines, jeden akt w wierszu: kolumny `index.csv`, `meta` = front matter, `markdown` = tekst bez front
  matter, `tree` = drzewo z pliku `.json`). Odświeżany codziennie po aktualizacji (workflow „Eksport”).
  Przykład: `pandas.read_json("monitor-polski-md.jsonl.gz", lines=True)`.
- Ten sam zbiór na Hugging Face (Parquet, drzewo jako tekst JSON): [huggingface.co/datasets/PolskiAgentW/monitor-polski-md](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-md),
  `datasets.load_dataset("PolskiAgentW/monitor-polski-md")`. Odświeżany razem z plikiem JSON Lines.

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
- **Lata 2012–2024** (15 885 aktów, przekonwertowane 2026-09-29/30 wersjami eli2md 0.6.7–0.6.17; zmiany 0.6.8–0.6.12
  dotyczą wydań z lat 2000–2011, a 0.6.13–0.6.17 tylko obsługi pamięci przy konwersji, wersja jest w kolumnie
  `converter`). Ta sama miara co niżej (`eval/selfcheck.py`), wszystkie akty:
  2012–2019 (9577 aktów, 0.6.7): mediana odsetka słów PDF obecnych w wyniku **0.986**, odwrotnie **0.994**;
  poniżej 0.95: 416 aktów (4,3%), poniżej 0.8: 16.
  2020–2024 (6308 aktów, 0.6.7–0.6.17): mediana **0.988**, odwrotnie **0.995**; poniżej 0.95: 248 (3,9%), poniżej
  0.8: 10. Najniższe wyniki mają m.in. akty, w których ten sam tekst jest w PDF wydrukowany kilka razy z przesunięciem
  (MP/2016/1000), oraz akty z wieloma stronami bez warstwy tekstowej, czytanymi przez OCR (MP/2023/1119: 398 z 1394
  stron, w tym obrócone tabele, z których OCR robi strzępy znaków). Wyniki dla każdego aktu:
  [eval/selfcheck_mp_2012_2019_v0.6.7.json](https://github.com/PolskiAgentW/eli2md/blob/main/eval/selfcheck_mp_2012_2019_v0.6.7.json),
  [eval/selfcheck_mp_2020_2024_v0.6.17.json](https://github.com/PolskiAgentW/eli2md/blob/main/eval/selfcheck_mp_2020_2024_v0.6.17.json).
  Kontrola wzrokowa lat 2012–2024: tylko 2 akty (MP/2013/393 bez uwag; MP/2013/567: tabela spłaszczona, jak opisano wyżej).
- **Czy tekst nie ginie** (`eval/selfcheck.py` z eli2md, wszystkie 2272 akty 2025–2026, eli2md 0.6.3, 2026-09-30):
  porównuję słowa wyniku ze słowami warstwy tekstowej PDF (bez winiety i nagłówków stron, bez stron czytanych
  przez OCR). Mediana odsetka słów PDF obecnych w wyniku: **0.985**, odwrotnie (słowa wyniku obecne w PDF):
  **0.993**. Poniżej 0.95: 80 aktów, poniżej 0.8: żaden. Z tych 80 aż 65 to krótkie akty (poniżej 400 słów), w których
  warstwa tekstowa PDF zawiera ukrytą kopię nagłówka wklejonego załącznika; konwerter ją celowo pomija
  (sprawdzone na MP/2025/613). W MP/2025/121 (0.876) część stron PDF ma dwie nałożone kopie tekstu, które miara
  czyta jako strzępy liter; to one są w większości „brakującymi słowami”. Kolejności słów ani podziału na jednostki
  ta miara nie sprawdza. Miara od 29.09 się zmieniła (strony obrócone, znak wodny, indeksy w nawiasach), więc
  wcześniejsze wyniki nie są z tymi porównywalne.
- **Kontrola wzrokowa** (strona PDF obok wyniku), 8 aktów: MP/2025/418 (s. 34), 613 (s. 1–2), 241 (s. 6, OCR),
  MP/2026/580 oraz — na próbnej konwersji wersją rozwojową 0.6.2.dev0 — MP/2025/113, 148, 158: tekst
  i akapity zgodne z PDF. W OCR zdarzają się błędy znaków (w MP/2025/241 „m²” odczytane jako „m””). MP/2025/121:
  w ciasno złożonej tabeli pozycje „2) … 5)” były doklejone do „1)”; od eli2md 0.6.3 zaczynają nowe akapity
  (229 → 535 akapitów w pliku). Wybór częściowo losowy,
  częściowo celowy (długie akty, OCR, najniższe wyniki miary powyżej).
- **Losowa kontrola wzrokowa** (2026-09-29, eli2md 0.6.2): 15 losowych aktów, 20 stron (strona 1 i jedna losowa).
  Bez żadnego błędu: 14 stron. Błąd konwertera: 6 stron — 2 istotne (MP/2025/635: pozycje listy odznaczonych
  sklejone w jeden akapit; MP/2025/1248: numerowany wiersz tabeli wzięty w JSON za ust. 8, pod który trafiły
  lit. e–i), 2 znanego typu (umowa MP/2026/869: s. 1 to obraz tekstu bez OCR, na s. 13 błędy OCR), 2 drobne
  (podpis, tytuł sklejony przez granicę strony). Na żadnej stronie z warstwą tekstową nie zginęło słowo. Próba
  mała (przedział 95%: 12–54% stron z błędem), 10 z 15 aktów ma 1 stronę. Raport:
  [eval/visual_audit_2025_2026_v0.6.2.md](https://github.com/PolskiAgentW/eli2md/blob/main/eval/visual_audit_2025_2026_v0.6.2.md).
  Metadane z API bywają błędne: MP/2025/635 ma `promulgation_date` 2025-07-08, PDF — 11 lipca 2025 r;
  MP/2026/615 miało `announcement_date` 2206-06-11, w tytule „z dnia 11 czerwca 2026 r.” (stan na 2026-09-30);
  API poprawiło tę datę 2026-10-01 na 2026-06-11, zbiór ma już nową wartość. 2026-10-02 API poprawiło kolejne
  daty, w tym 30 w tym zbiorze (23 `announcement_date`, 7 `promulgation_date`; teraz zgodne z PDF); nowe wartości
  są tu od aktualizacji 2026-10-03.
- **Zmiana w eli2md 0.6.22** (2026-10-02 w nocy; 202 akty, w których OCR nie dał tekstu z części stron): strona skanu,
  z której OCR nie odczytał użytecznego tekstu, jest czytana drugi raz z podaną rozdzielczością obrazu (wcześniej
  tesseract jej nie dostawał i na stronach z tabelami gubił odstępy między słowami). Strony odczytane wcześniej czyta
  się jak przedtem. W tych 202 aktach: strony z tekstem z OCR 7039 → 7100, słowa 2 049 238 → 2 056 532; tekst zmienił się
  w 24 plikach, w żadnym akcie nie ubyło stron z OCR. Akty przeliczone lokalnie (w workflow nie mieściły się w limicie czasu).
- **Zmiana w eli2md 0.6.7** (akty od nowa 2026-09-30 około 10:00; tekst zmienił się w 20 plikach): objaśnienia
  wydrukowane w treści (pod tabelami, w formularzach) mają znaczniki `¹⁾` jak w druku, a nie `[^n]` prowadzące do
  przypisu aktu o tym numerze; przypis z wyliczeniem („1) …”, „2) …”) jest w całości przypisem. Selfcheck: lepiej
  w 16 plikach, gorzej w 1 (o 0,0002).
- **Zmiana w eli2md 0.6.5** (akty od nowa 2026-09-30 przed południem; tekst i JSON zmieniły się w 4 plikach):
  przypisy spod kreski narysowanej linią albo położonej wysoko na stronie są definicjami `[^n]:`, a nie treścią
  (MP/2025/605: 8 przypisów do tabeli współczynników waloryzacji). Selfcheck bez zmian.
- **Zmiana w eli2md 0.6.4** (akty od nowa 2026-09-30 rano; tekst zmienił się w 11 plikach, drzewo JSON w 12):
  s. 1 umów międzynarodowych, na której preambuła i pierwsze artykuły są obrazem, czyta OCR, jeśli obraz wygląda
  na tekst ciągły (MP/2026/869: preambuła, art. 1 pkt 1–2). Tekst jest oznaczony notką i cytatami `> …`, jak inny
  OCR. W JSON numerowane wiersze tabel nie są jednostkami (MP/2025/1248: lit. e–i są teraz pod pkt 2).
- **Poprawione w eli2md 0.6.3** (dane przekonwertowane od nowa 2026-09-30; tekst zmienił się w 37 plikach):
  w wklejonych PDF-ach konwerter gubił litery czcionek z błędnymi metrykami, np. „elekt omobinos ci” zamiast
  „elektromobilności” w MP/2025/1128 (odsetek słów 0.72 → 0.997). W MP/2025/541 (obrócona tabela z drobnym
  drukiem, s. 46–48) niska wartość (0.785) wynikała głównie z miary, która czytała kolumny obróconej tabeli
  na przemian. Konwerter gubił tam też część liter (usuwał je jako duplikaty). Teraz 0.991 (nowa miara).
- **Struktura** (art./§/ust./pkt/lit., drzewo JSON) jest zmierzona tylko na Dzienniku Ustaw 2024 (README eli2md).
  Obejrzane akty Monitora Polskiego mają podobny układ jak Dziennik Ustaw, ale struktury tu nie mierzyłem.
<!-- quality:end -->

Błędy konwersji zgłaszaj w Issues. Najlepiej podaj pozycję aktu i fragment.

Aktualizacja: codziennie o 04:53 UTC workflow `.github/workflows/update.yml` pobiera listę aktów
z API ELI (lata od 2012). GitHub potrafi opóźnić taki start o kilka godzin, więc jeśli do 10:17 UTC nie było
udanej aktualizacji, workflow rusza drugi raz. Konwertuje nowe akty oraz te, którym zmienił się `changeDate`, i commituje wynik.
Lata 2012–2024 zostały przekonwertowane jednorazowo 2026-09-30.
Jeśli przez ponad 10 dni nie przybędzie żaden nowy akt, workflow kończy się błędem, żeby cicha awaria
była widoczna. Najdłuższa przerwa w ogłaszaniu aktów w Monitorze Polskim w latach 2025–2026 wyniosła 6 dni.

Zmiana 2026-10-10 (drzewo JSON, kod drzewa eli2md 0.6.50, 14 aktów; opis w README eli2md, wpis 0.6.50): nagłówki z
liczebnikiem słownym („DZIAŁ PIĄTY”, „CZĘŚĆ PIERWSZA”), z numerem rzymskim z wielką literą („DZIAŁ IVA”) albo z
odnośnikiem po numerze („Rozdział 5a[^28]”) są w `.json` węzłami `heading`. Wcześniej trafiały jako tekst do artykułu,
paragrafu albo punktu przed nimi. Nowych nagłówków: 35, żaden nie zniknął. `.md` się nie zmienił, więc pole
`converter` (w `.md`, `.json` i `index.csv`) zostaje wersją, w której powstał `.md`. Słowa w drzewach: zgubione 0.
Pozostałe akty bez zmian (porównanie drzew wszystkich aktów zbioru). W MP/2019/1190 dodatkowo 11 artykułów umowy
(„Artykuł N”) jest węzłami `art` (zmiana kodu drzewa z 0.6.39): jednostek 26 → 37, żadna nie zniknęła, a ścieżki
jednostek zmieniły się tylko w tym akcie.

Od 2026-10-10 codzienna aktualizacja używa eli2md 0.6.50 (wcześniej 0.6.25.2). Sprawdzenie przed zmianą: 100
najnowszych aktów MP przeliczonych wersją 0.6.50 z tych samych PDF ma ten sam `.md` i `.json` co w zbiorze (poza
polem `converter`).

Zmiana 2026-10-05 (eli2md 0.6.25, 0.6.25.1 i 0.6.25.2 — ten sam wynik; wszystkie akty od nowa; wcześniej wersje
0.6.7–0.6.22, w większości 0.6.7). Zmienione 16 z 18 165 plików, w 10 z nich te same słowa: więcej nagłówków
jednostek w 5 plikach, więcej przypisów w 5, w żadnym mniej. Słowa: −138 / +433 w 6 plikach: notki o stronach z OCR
(nowe brzmienie, tesseract 5.5.0 zamiast 5.3.4), strony odczytane przez OCR, których wcześniej nie było (MP/2025/193,
MP/2025/253, MP/2023/1470: po 1–2 strony), a w MP/2015/614 litera po numerze normy jest sklejona z numerem
(„PN-57/B-024051a)” zamiast „PN-57/B-024051 a)”). Żaden plik nie stracił więcej niż 2% słów. Od 2026-10-05 workflow
aktualizacji używa eli2md 0.6.25.2.

## Licencja

Akty normatywne i ich urzędowe projekty oraz urzędowe dokumenty i materiały nie są przedmiotem prawa
autorskiego (art. 4 pkt 1 i 2 ustawy o prawie autorskim i prawach pokrewnych). Pozostała zawartość
(indeks, skrypty): CC0 1.0.
