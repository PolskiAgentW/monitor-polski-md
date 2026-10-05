---
language:
- pl
license: cc0-1.0
pretty_name: Monitor Polski od 2012 r. w Markdown/JSON
size_categories:
- 10K<n<100K
tags:
- legal
- law
- poland
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*.parquet
---

# Monitor Polski od 2012 r. — teksty aktów w Markdown/JSON

Nieoficjalne teksty wszystkich aktów z Monitora Polskiego ogłoszonych od 2012 r., przekonwertowane z urzędowych
PDF-ów otwartym konwerterem [eli2md](https://github.com/PolskiAgentW/eli2md). Odświeżane codziennie.

*Unofficial plain-text (Markdown) and structured (JSON tree of units) versions of all acts published in Monitor
Polski (the Polish official gazette) since 2012. The Sejm ELI API serves them only as PDF. Converted automatically;
the PDF is the binding text. Updated daily.*

**Dlaczego:** API ELI Sejmu nie ma HTML dla żadnego aktu Monitora Polskiego, tylko PDF.
Szczegóły: [repozytorium na GitHubie](https://github.com/PolskiAgentW/monitor-polski-md).

<!-- zbiory:start -->
**Wszystkie zbiory** (ten sam format plików, konwerter [eli2md](https://github.com/PolskiAgentW/eli2md)). Akty, które API ELI
podaje w HTML (np. większość Dziennika Ustaw 2012–2024), nie są tu powielane.

| lata | Dziennik Ustaw | Monitor Polski |
|---|---|---|
| od 2012 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-md): od 2025 r. wszystkie, wcześniej 98 aktów bez HTML; codziennie | [GitHub](https://github.com/PolskiAgentW/monitor-polski-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-md): wszystkie z PDF (API nie ma HTML); codziennie |
| 2000–2011 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-2000-2011-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-2000-2011-md): akty bez HTML w API | [GitHub](https://github.com/PolskiAgentW/monitor-polski-2000-2011-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-2000-2011-md): wszystkie z PDF |
| 1990–1999 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-1990-1999-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-1990-1999-md): akty bez HTML w API (OCR skanów) | brak |

Kolumny są we wszystkich zbiorach te same, więc lata można wczytać razem (nadal bez aktów, które API ELI podaje w HTML):

```python
from datasets import load_dataset

du = load_dataset("parquet", split="train", data_files=[
    "hf://datasets/PolskiAgentW/dziennik-ustaw-1990-1999-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-2000-2011-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-md/data/*.parquet",
])  # 30 018 aktów (2026-10-05); Monitor Polski: monitor-polski-2000-2011-md + monitor-polski-md
```
<!-- zbiory:end -->

## Użycie

```python
from datasets import load_dataset
import json

ds = load_dataset("PolskiAgentW/monitor-polski-md", split="train")
print(ds[0]["eli"], ds[0]["title"])
tree = json.loads(ds[0]["tree"])  # drzewo jednostek
```

## Kolumny

Jeden wiersz = jeden akt.
- `eli` (np. `MP/2025/613`), `year`, `pos`, `type`, `title`, `display_address`, `announcement_date`, `promulgation`,
  `entry_into_force`, `legal_status`, `keywords`, `change_date`, `source_pdf`, `pdf_sha256`: metadane z API ELI
  (bez poprawek, więc z jego błędami; `legal_status` — stan w chwili konwersji);
- `pages`, `words`, `no_text_pages`, `image_pages`, `ocr_pages`, `image_ocr_pages`: strony PDF, słowa wyniku,
  strony bez warstwy tekstowej (skany), strony z dużymi obrazami (ich treści brak), strony odczytane przez OCR,
  strony, na których OCR odczytał obraz tekstu (s. 1 umów międzynarodowych, od eli2md 0.6.4);
- `markdown`: tekst aktu (tekst z OCR jako cytaty `> …` z notką przed stroną);
- `tree`: ten sam akt jako drzewo jednostek w JSON (tekst; opis formatu w
  [README eli2md](https://github.com/PolskiAgentW/eli2md#json-drzewo-jednostek-od-053));
- `converter`, `converted_at`: wersja eli2md i czas konwersji.

## Jakość

Dla Monitora Polskiego nie ma wzorca (HTML), więc jakość jest sprawdzana słabiej niż dla Dziennika Ustaw:
porównanie słów wyniku z warstwą tekstową PDF (mediana odsetka słów PDF obecnych w wyniku 0.985, 2272 akty)
i losowa kontrola wzrokowa (20 stron: 14 bez błędu). Znane błędy i szczegóły:
[README na GitHubie](https://github.com/PolskiAgentW/monitor-polski-md#jak-powstaje-i-jak-dobre-jest).

**To nie jest urzędowy tekst.** Wiążący jest PDF w Monitorze Polskim (`source_pdf`). Błędy konwersji zgłaszaj
w [Issues na GitHubie](https://github.com/PolskiAgentW/monitor-polski-md/issues).

## Źródło i licencja

Źródło: [API ELI Sejmu](https://api.sejm.gov.pl/eli/acts/MP). Ten sam zbiór jako pliki `.md`/`.json`:
[github.com/PolskiAgentW/monitor-polski-md](https://github.com/PolskiAgentW/monitor-polski-md).
Monitor Polski 2000–2011: [PolskiAgentW/monitor-polski-2000-2011-md](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-2000-2011-md).
Akty normatywne i urzędowe dokumenty nie są przedmiotem prawa autorskiego (art. 4 pkt 1 i 2 ustawy o prawie
autorskim i prawach pokrewnych); pozostała zawartość: CC0 1.0.
