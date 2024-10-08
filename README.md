# Projekt zaawansowanego kalkulatora

## Krótki opis projektu

Projekt zakłada stworzenie zaawansowanego kalkulatora - aplikacji stworzonej w języku Python, która umożliwi użytkownikowi wykonywanie zaawansowanych operacji matematycznych za pomocą interfejsu graficznego. Projekt jest realizowany przez Wojciecha Kuźbińskiego oraz Michała Michalskiego w ramach przedmiotu "Modelowanie i analiza systemów informatycznych" na pierwszym roku studiów magisterskich kierunku Informatyka na UMK w Toruniu.

## Funkcje

- Dodawanie, odejmowanie, mnożenie i dzielenie liczb.
- Wykonywanie zaawansowanych operacji matematycznych, takich jak potęgowanie, pierwiastkowanie, funkcje trygonometryczne itp.
- Wyświetlanie wykresów funkcji przy użyciu biblioteki matplotlib.
- Możliwość zapisywania i wczytywania danych do/z pliku.

## Wykorzystane technologie

Aplikacja korzysta z następujących technologii i bibliotek:

- **_PySide_**: Biblioteka do tworzenia interfejsów użytkownika w Pythonie; jest oparta o framework Qt.
- **_Matplotlib_**: Biblioteka do tworzenia wykresów i wizualizacji danych w Pythonie.
- **_Sympy_**: Biblioteka do symbolicznego obliczania matematycznego, umożliwiająca manipulację i rozwiązywanie równań matematycznych oraz operacje na wyrażeniach algebraicznych.

## Instalacja projektu

Aby uruchomić kalkulator na swoim komputerze, wykonaj następujące kroki:

1. Sklonuj repozytorium na swoje urządzenie:

W oknie konsoli wpisz komendę:

```bash
$ git clone https://github.com/di0xinho/MiASI_projekt.git
```

2. Przejdź do katalogu z aplikacją:

```bash
$ cd MiASI_projekt
```

3. Zainstaluj wszystkie potrzebne biblioteki, aby móc odpalić aplikację:

```bash
$ pip install -r requirements.txt
```

4. Uruchom aplikację stosując polecenie:

```bash
$ python mainwindow.py
```

## Instrukcja obsługi

### Pierwsza zakładka - kalkulator naukowy

Domyślną zakładką po uruchomieniu aplikacji jest zakładka z kalkulatorem naukowym.
Zakładka składa się z kilku części:

- części do wprowadzania formuły matematycznej,
- części pokazującej wynik formuły matematycznej,
- klawiatury do wprowadzania formuły matematycznej,
- historii obliczeń podczas trwania działania aplikacji

<div align="center">
  <img src="images/1.png" width="100%">
</div>

Po wprowadzeniu formuły matematycznej do pola znajdującego się najwyżej, możemy kliknąć przycisk "=",
aby obliczyć działanie. Przypadek ten demonstruje ilustracja znajdująca się niżej.

<div align="center">
  <img src="images/2.png" width="100%">
</div>

Wyniki obliczonych formuł trafiają do historii po prawej stronie okna. Historię obliczeń możemy usunąć
klikając przycisk "Wyczyść historię" na samej górze listy.

### Druga zakładka - narzędzie do rysowania wykresów

Aby skorzystać z narzędzia do rysowania wykresów musimy przełączyć się na drugą zakładkę.
Po przełączeniu ujrzymy to co przedstawia ilustracja poniżej.

<div align="center">
  <img src="images/3.png" width="100%">
</div>

Zakładka składa się z następujących części:

- listy funkcji, gdzie można stworzyć sformułowaną przez siebie funkcję,
- wykresu funkcji (domyślnie wykres jest pusty),
- klawiatury do wprowadzania funkcji

Aby utworzyć nową funkcję należy kliknąć na znak "+" na liście po lewej stronie. Po wykonaniu tej czynności pojawi się
szablon funkcji, który należy wypełnić klikając na przycisk edycji. Po kliknięciu pole to stanie się polem edycyjnym,
klawiatura zostanie uaktywniona. W tym momencie będziemy mogli wprowadzić wyrażenie, które będziemy chcieli potem
wyświetlić na wykresie. Aby pole przestało być polem edycyjnym należy kliknąć na przycisk edycji ponownie - wtedy
też kolor przycisku zmieni swój kolor. Aby narysować wykres trzeba zaznaczyć checkbox znajdujący się obok pola z
formułą, a następnie kliknąć przycisk "Rysuj wykres". Po naciśnięciu przycisku wykres pojawia się obok listy z funkcjami.
Użytkownik aplikacji jest w stanie utworzyć maksymalnie 10 funkcji.

W ramach analizy można:

- przybliżać/oddalać wykres,
- zmieniać edytować osie,
- przesuwać wykres,
- zapisać zdjęcie wykresu do pliku

<div align="center">
  <img src="images/4.png" width="100%">
</div>
