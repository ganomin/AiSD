# Odpowiedzi na pytania w zadaniu

## Wynik programu

```terminaloutput
Eksperyment 1:
α    | średnia liczba prób (sukces) | średnia liczba prób (porażka) | max prób
------------------------------------------------------------------------------
0.25 |                        70.42 |                          1.00 | 803
0.50 |                       453.96 |                          1.06 | 1622
0.75 |                       858.17 |                        723.79 | 2558
0.90 |                      1109.87 |                       1239.79 | 3075

Eksperyment 2:
α    | średnia liczba prób (sukces) | średnia liczba prób (porażka) | max prób
------------------------------------------------------------------------------
0.52 |                       864.72 |                        723.79 | 2546
```

## Eksperyment 1

### Przy jakim α tablica przestaje działać efektywnie?

Zauważamy, że gdy współczynnik alfa (czyli stosunek liczby elementów do wielkości tablicy) przekracza 0.5, wydajność
drastycznie spada, ponieważ pojedyncze kolizje zaczynają się łączyć w długie, coraz większe, nieprzerwane ciągi zajętych
komórek.

### Która operacja pogarsza się najbardziej?

Najbardziej degraduje się operacja wyszukiwania nieistniejących kluczy, ponieważ algorytm musi przeszukiwać cały duży,
nieprzerwany ciąg zajętych komórek, aby ostatecznie natknąć się na wartość 'None'.

## Eksperyment 2

### Czy liczba prób rośnie?

Nie, utrzymuje się na podobnym (czasem lekko wyższym) poziomie.

### Jaki wpływ mają „dziury” (DEL)?

Znacznik 'DEL' funkcjonuje tak samo, jak inna zajęta komórka w tablicy. Mimo że usuniemy część danych i nasz
współczynnik alfa (liczba elementów / rozmiar tablicy) maleje, to algorytm nadal iteruje po wartościach 'DEL', dopóki
nie natknie się na szukaną wartość lub None. 
