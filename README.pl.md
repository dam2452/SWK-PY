# Skrypt Pobierania SWK

Ten skrypt Python umożliwia pobieranie odcinków "Świat Według Kiepskich" z obsługą wznawiania. Obsługuje pobieranie odcinków według sezonu lub numerów globalnych, a także zawiera funkcje takie jak usuwanie częściowych pobrań i śledzenie postępu.

## Ważna Informacja

**Zrzeczenie:** Nie jestem autorem ani twórcą pliku `.txt`, jego zawartości ani żadnych linków w nim zawartych. Nie mam żadnego powiązania z właścicielami lub twórcami "Świat Według Kiepskich" ani żadnych powiązanych treści. "Świat Według Kiepskich" jest własnością Polsatu, a wszystkie prawa do serialu należą do nich. Nie ponoszę odpowiedzialności za zawartość pliku `.txt` ani za to, jak jest używany. Ten skrypt jest jedynie narzędziem napisanym w Pythonie, które pomaga w pobieraniu odcinków wymienionych w dostarczonym pliku `.txt`.

## Dostępne wersje językowe

- [Polski (Ten plik)](README.pl.md)
- [English (Angielski)](README.md)

## Prosty Przewodnik Instalacji

Jeśli nie znasz się na programowaniu lub instalowaniu oprogramowania, postępuj zgodnie z tymi krokami, aby wszystko skonfigurować. Ten przewodnik pomoże Ci zainstalować niezbędne narzędzia i uruchomić skrypt w prosty sposób.

### Krok 1: Zainstaluj Git

Git jest systemem kontroli wersji, który pomoże Ci pobrać skrypt z GitHuba.

1. Otwórz **Wiersz polecenia** (`cmd`). Możesz to zrobić, wpisując `cmd` w menu Start i naciskając Enter.
2. Wpisz następujące polecenie i naciśnij Enter:

   ```bash
   winget install --id Git.Git -e --source winget
   ```

3. Poczekaj na zakończenie instalacji.

### Krok 2: Zainstaluj Pythona

Python to język programowania używany do uruchamiania tego skryptu.

1. W tym samym oknie Wiersza polecenia wpisz następujące polecenie i naciśnij Enter:

   ```bash
   winget install --id Python.Python.3.12 -e --source winget
   ```

2. Poczekaj na zakończenie instalacji.

### Krok 3: Pobierz Skrypt

1. Po zainstalowaniu Git, wpisz następujące polecenie, aby pobrać skrypt z GitHuba:

   ```bash
   git clone https://github.com/dam2452/SWK-PY
   ```

2. Przejdź do katalogu ze skryptem:

   ```bash
   cd SWK_download
   ```

### Krok 4: Zainstaluj Wymagane Biblioteki Pythona

1. Przed uruchomieniem skryptu musisz zainstalować kilka bibliotek Pythona. W tym samym oknie Wiersza polecenia wpisz:

   ```bash
   pip install requests tqdm
   ```

2. Poczekaj na zakończenie instalacji.

### Krok 5: Uruchom Skrypt

Teraz jesteś gotowy, aby pobrać odcinki!

- **Aby pobrać wszystkie odcinki przy użyciu domyślnych ustawień**, po prostu wpisz:

  ```bash
  python SWK_download.py
  ```

- **Aby pobrać konkretny odcinek (np. odcinek 166)**, wpisz:

  ```bash
  python SWK_download.py --episode 166
  ```

- **Aby pobrać wszystkie odcinki z konkretnego sezonu (np. sezon 3)**, wpisz:

  ```bash
  python SWK_download.py --season 3
  ```

Odcinki zostaną pobrane do folderu `SWK_downloaded` w tym samym katalogu, w którym znajduje się skrypt.

## Funkcje

- **Obsługa wznawiania**: Automatyczne wznawianie pobrań od miejsca, w którym zostały przerwane.
- **Paski postępu**: Wyświetla paski postępu w czasie rzeczywistym zarówno dla pojedynczych odcinków, jak i całkowitego postępu pobierania.
- **Usuwanie częściowych plików**: Usuwa niekompletne pliki przed rozpoczęciem nowej sesji pobierania.
- **Elastyczne tryby numeracji**: Obsługuje zarówno numerację opartą na sezonach, jak i numerację globalną odcinków.
- **Selektowne pobieranie**: Umożliwia pobieranie konkretnego odcinka lub wszystkich odcinków z wybranego sezonu.

## Wymagania

- Python 3.6 lub nowszy
- Biblioteka `requests`
- Biblioteka `tqdm`

Te wymagania są automatycznie instalowane, jeśli postępujesz zgodnie z Przewodnikiem Instalacji powyżej.

## Użycie

### Domyślne Użycie

Jeśli chcesz użyć domyślnego pliku wejściowego (`kiepscy.txt` w katalogu ze skryptem) i wyjściowego (`SWK_downloaded` w katalogu ze skryptem), po prostu uruchom:

```bash
python SWK_download.py
```

### Niestandardowe Użycie

Możesz dostosować ścieżki pliku wejściowego i katalogu wyjściowego, używając opcji `--input` i `--output`:

```bash
python SWK_download.py --input /ścieżka/do/twojego/kiepscy.txt --output /ścieżka/do/katalogu/wyjściowego
```

### Pobieranie Konkretnego Odcinka

Aby pobrać konkretny odcinek według jego numeru globalnego:

```bash
python SWK_download.py --episode 166
```

### Pobieranie Pełnego Sezonu

Aby pobrać wszystkie odcinki z konkretnego sezonu:

```bash
python SWK_download.py --season 3
```

## Format Pliku Wejściowego

Plik wejściowy (`kiepscy.txt`) powinien wymieniać sezony i URL-e odcinków w następującym formacie:

```plaintext
SEZON 1
http://example.com/episode1.mp4
Nazwa Odcinka 1
http://example.com/episode2.mp4
Nazwa Odcinka 2

SEZON 2
http://example.com/episode3.mp4
Nazwa Odcinka 3
```

## Przykład

Oto przykład uruchomienia skryptu w celu pobrania wszystkich odcinków z sezonu 3:

```bash
python SWK_download.py --season 3
```

## Wkład

Wkłady, problemy i prośby o nowe funkcje są mile widziane! Zapraszamy do sprawdzenia [strony problemów](https://github.com/yourusername/SWK_download/issues).

## Licencja

Ten projekt jest licencjonowany na otwartej licencji, co pozwala każdemu na używanie, modyfikowanie i rozpowszechnianie kodu bez ograniczeń.