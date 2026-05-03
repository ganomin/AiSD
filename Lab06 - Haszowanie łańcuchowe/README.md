# Haszowanie łańcuchowe

## Przykład najprostszej funkcji haszującej

```python
list_to_hash = ["abc", "bcd", "cde", "def"]

hash_table = []
hash_table_size = 2

for _ in range(hash_table_size):
    hash_table.append([])

for element in list_to_hash:
    ascii_value = ord(element[0]) % hash_table_size
    hash_table[ascii_value].append(element)

print(hash_table)
```

## Dane wejściowe

Jako danych wejściowych do wstawienia do tablicy haszującej użyjemy 5000 pierwszych słów
z [listy najpopularniejszych polskich słów](https://raw.githubusercontent.com/frekwencja/most-common-words-multilingual/refs/heads/main/data/wordfrequency.info/pl.txt).

## Parametry eksperymentu

### Wybór parametru `m`

Jako parametru `m`, który jest naszym rozmiarem tablicy, musimy użyć trzech różnych liczb pierwszych.

Używamy liczb pierwszych, ponieważ ich właściwość dzielenia się tylko przez 1 i samą siebie, pozwala na bardziej
równomierne wstawienie danych do tablicy haszującej, ograniczając występowanie kolizji.

Jako konkretnych wartości użyjemy trzech liczb pierwszych w zakresie od 0 do 2500 (by z puli 5000 słów móc wstawić około
`2 * m` elementów).

Takimi liczbami będą liczby zbliżone do wyników podziału maksymalnego zakresu 2500 na 3 równe części:

- 839 (najbliższa liczba pierwsza do 833)
- 1667 (najbliższa liczba pierwsza do 1666)
- 2503 (najbliższa liczba pierwsza do 2499)

### Wybór funkcji haszujących `h1` i `h2`

Jako pierwszą funkcję haszującą `h1` wybierzemy lekko zmodyfikowany algorytm z przykładu wyżej, polegający na haszowaniu
bazując na wartości ASCII znaków.

Jednakże do obliczenia indeksu zamiast wartości ASCII tylko pierwszej litery, użyjemy sumy całego wyrazu, ponieważ wiele
słów zaczyna się na tę samą literę, co przy sprawdzaniu tylko jednego znaku generowałoby ogromną liczbę kolizji. Użycie
sumy wszystkich znaków pozwoli znacznie lepiej rozproszyć dane.

Jednakże ta funkcja ma swoją wadę, dla anagramów będzie ona dawała taką samą sumę, powodując niepotrzebne kolizje.

Możemy to rozwiązać, używając algorytmu haszowania wielomianowego (będzie naszą funkcją `h2`), który uwzględnia pozycję
litery w słowie. Polega on na przemnożeniu wartości ASCII każdego pojedynczego znaku przez stałą liczbę pierwszą
podniesioną do potęgi równej pozycji tej litery w wyrazie.

## Przebieg eksperymentu

Kod programu: [main.py](main.py)

## Prezentacja wyników

```terminaloutput
python3 main.py

m    | funkcja haszująca | liczba pustych list | maks. długość listy | średnia długość niepustych list
-------------------------------------------------------------------------------------------------------
839  | h1                | 12                  | 21                  | 6.05
839  | h2                | 3                   | 20                  | 5.98
-------------------------------------------------------------------------------------------------------
1667 | h1                | 406                 | 18                  | 3.97
1667 | h2                | 179                 | 15                  | 3.36
-------------------------------------------------------------------------------------------------------
2503 | h1                | 1195                | 18                  | 3.82
2503 | h2                | 526                 | 13                  | 2.53
-------------------------------------------------------------------------------------------------------
```

## Analiza i porównanie

Zauważamy, że funkcja `h2` niezależnie od rozmiaru tablicy zawsze znacznie lepiej sobie radzi niż prosta suma znaków
`h1`, ponieważ generuje ona krótsze kolizje z łańcuchami list. Widzimy również, że zwiększenie rozmiaru `m` w obu
funkcjach redukuje średnią i maksymalną długość list.

Odpowiedzi na pytania:

1. Który wariant daje najmniej kolizji?

- Odpowiedź: Drugi wariant, ponieważ nawet dla podobnych do siebie danych poprzez osobne wymnożenie każdego znaku ASCII,
  wylicza różne wartości indeksu.

2. Jak zmiana `m` wpływa na rozkład elementów?

- Odpowiedź: Im większe `m`, tym więcej miejsca dla elementów (zmniejsza się współczynnik wypełnienia). Zmniejsza to
  liczbę kolizji i skraca łańcuchy list, ale kosztem tego, że tworzy się więcej pustych list.

3. Która funkcja haszująca lepiej rozprasza dane?

- Odpowiedź: Druga funkcja `h2`, ponieważ funkcja `h1` sumuje znaki, co daje identyczny hasz dla anagramów (np. "kot"
  i "tok"). Funkcja wielomianowa `h2` uwzględnia pozycję litery w słowie i dzięki temu każde unikalne słowo daje inny
  wynik, co o wiele bardziej rozprasza dane.

Uzasadnienia:

1. Wybór wartości `m`:

- Odpowiedź: Mieliśmy wstawić do tablicy około `2 * m` kluczy (więc dwa razy więcej niż wielkość tablicy). Podzieliłem
  maksymalną wielkość tablicy (2500) na trzy, by utrzymać małą, średnią i dużą wielkość `m`, następnie wyszukałem
  najbliższą liczbę pierwszą dla tych liczb.

2. Wybór funkcji haszujących:

- Odpowiedź: Funkcję `h1` wybrałem jako poprawioną wersję krótkiego algorytmu haszującego bazującego na wartości ASCII,
  jednakże jak wyżej już wspomniałem, ma ona problem, z tym że generuje taką samą wartość haszu dla anagramów danego
  słowa. Rozwiązaniem tego problemu było znalezienie [sposobu](https://en.wikipedia.org/wiki/Rolling_hash), by rozróżnić
  dane anagramy od siebie.

3. Zależności między rozmiarem tablicy a liczbą kolizji:

- Odpowiedź: Liczba kolizji maleje wraz ze wzrostem rozmiaru tablicy. Wynika to losowości, im mamy więcej dostępnych
  indeksów do użycia do tej samej liczby kluczy, szansa na trafienie w to samo miejsce znacznie spada.

## Wniosek/finalna odpowiedź

### Który wariant jest lepszy i dlaczego?

Dobrą funkcję haszującą cechuje niska ilość kolizji i równomierny rozkład, dlatego najlepszym wariantem jest funkcja
`h2` z rozmiarem `m = 2503`. Generuje ona najkrótszą długość niepustych list i najkrótszą maksymalną długość listy.
