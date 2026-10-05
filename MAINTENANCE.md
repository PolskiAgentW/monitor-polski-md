# Utrzymanie

Jak działa automatyczna aktualizacja tego zbioru, co może przestać działać i jak to sprawdzić albo naprawić.
Stan na 2026-10-05.

## Co działa samo

- `.github/workflows/update.yml` („Aktualizacja”): codziennie o 04:53 UTC i zapasowo o 10:17 UTC (tylko gdy tego dnia
  nie było udanej aktualizacji) pobiera z API ELI listę aktów Monitora Polskiego od 2012 r., konwertuje akty, które mają tylko
  tekst PDF (bez HTML): nowe oraz te, którym zmienił się `changeDate` (eli2md, OCR tesseract), aktualizuje statystyki w README i commituje wynik.
  Kończy się błędem, jeśli najnowszy akt w `index.csv` ogłoszono ponad 10 dni temu (zielony run bez nowych aktów
  wygląda jak zdrowy).
- `.github/workflows/export.yml` („Eksport”): po każdej aktualizacji buduje plik z całym zbiorem (wydanie „dane” na GitHubie,
  `.jsonl.gz`) i parquet na Hugging Face (`huggingface.co/datasets/PolskiAgentW/monitor-polski-md`). Potrzebuje sekretu repozytorium `HF_TOKEN`.
- W `update.yml` przypięte są: wersja konwertera (`eli2md@v0.6.25.1`), jego zależności (pdfplumber, pdfminer.six,
  pypdfium2, pillow) i obraz serwera (`ubuntu-24.04`, tesseract 5.3.4 z pakietów systemu).

## Jak sprawdzić, czy działa

- Zakładka Actions: ostatni run „Aktualizacja” z dzisiaj albo wczoraj, zielony. Albo:
  `gh run list -R PolskiAgentW/monitor-polski-md -w update.yml -L 5`.
- README, sekcja „Stan”: data i godzina ostatniego przeliczenia statystyk.
- Ręczne uruchomienie: Actions → Aktualizacja → Run workflow (albo `gh workflow run update.yml -R PolskiAgentW/monitor-polski-md`).

## Co może przestać działać

| Objaw | Możliwa przyczyna | Co zrobić |
|---|---|---|
| Brak runów z harmonogramu | GitHub wyłącza harmonogram w publicznym repo po 60 dniach bez aktywności. Workflow commituje codziennie, ale czy commity bota liczą się jako aktywność, nie wiem | Actions → Aktualizacja → Enable workflow |
| Run z harmonogramu o kilka godzin później albo wcale | Opóźnienia GitHuba (2026-10-04: 4–7 h) | Nic; termin zapasowy 10:17 UTC |
| „Kontrola świeżości” czerwona | Brak nowych aktów przez ponad 10 dni: API ELI nie zwraca nowych aktów, zmienił się jego format albo pobieranie się nie udaje | Log kroku „Nowe i zmienione akty”; porównać z api.sejm.gov.pl/eli/acts/MP/<rok> |
| Eksport czerwony | `HF_TOKEN` unieważniony albo zmiana po stronie Hugging Face | Nowy token z prawem zapisu → Settings → Secrets → `HF_TOKEN` |
| Błąd instalacji eli2md | Repo github.com/PolskiAgentW/eli2md niedostępne | Bez tego repo konwersja nie ruszy |
| Akt z `status=error` w `index.csv` | PDF, którego konwerter nie umie przeczytać, albo przekroczony limit pamięci (`--mem-limit-gb`, domyślnie 3 GB) | Akt jest próbowany ponownie w każdym runie; pozostałe akty to nie blokuje (od 0.6.25.1) |

## Zmiana wersji konwertera

1. Nowa wersja eli2md z tagiem.
2. Lokalnie przeliczyć cały zbiór nową wersją (`python -m eli2md.dataset --root . --years $(seq 2012 2026) --all --json
   --ocr --publisher MP`) i porównać z opublikowanym (liczba słów na plik, pliki ze stratą
   słów).
3. Dopiero potem zmienić pin w `update.yml`; inaczej zbiór miesza wyniki dwóch wersji.

