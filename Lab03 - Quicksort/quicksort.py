# Zadanie 3.B
from random import randint
from time import perf_counter


# Algorytm Quicksort
def quicksort(A, low, high):
    """ Implementacja bazuje na pseudokodzie z wykładu
        oraz https://en.wikipedia.org/wiki/Quicksort
        Złożoność: O(n * log n), w najgorszym: O(n^2) """

    # Warunek rekurencyjny
    if low >= high or low < 0:
        return None

    # Podziel i zapamiętaj punkt podziału (pivot)
    p = partition(A, low, high)

    # Posortuj lewy i prawy podział i rekurencję
    quicksort(A, low, p - 1)  # Lewa strona
    quicksort(A, p + 1, high)  # Prawa strona

    return A


# Algorytm na podział tablicy
def partition(A, low, high):
    """ Implementacja bazuje na pseudokodzie z https://pl.wikipedia.org/wiki/Sortowanie_szybkie
        oraz na "Lomuto partition scheme" z https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
        Złożoność: O(n) """

    # Losujemy element spośród naszej listy i wybieramy go jako punkt podziału (pivot).
    # W przeciwieństwie do standardowego podejścia i wyboru ostatniego elementu jako pivotu,
    # dzięki naszemu podejściu drastycznie redukujemy czas wykonywania algorytmu (szczegóły na końcu programu).
    random_pivot_index = randint(low, high)
    A[high], A[random_pivot_index] = A[random_pivot_index], A[high]

    # Wyznaczamy (wcześniej wylosowany) punkt podziału (pivot)
    pivot = A[high]

    # Zmienna pomocnicza
    i = low

    # Przechodzimy po tablicy i przyrównujemy do pivota
    for j in range(low, high):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    # Umieszczamy pivot na swoje posortowane miejsce
    A[i], A[high] = A[high], A[i]

    return i


# Wypełnij listę losowymi liczbami
def insert_random(n):
    list_of_numbers = []
    for num in range(0, n):
        list_of_numbers.append(randint(0, n))
    return list_of_numbers


# Wypełnij listę liczbami rosnąco
def insert_ascending(n):
    list_of_numbers = []
    for num in range(1, n + 1):
        list_of_numbers.append(num)
    return list_of_numbers


# Wypełnij listę liczbami malejąco
def insert_descending(n):
    list_of_numbers = []
    for num in range(n, 0, -1):
        list_of_numbers.append(num)
    return list_of_numbers


# Uruchamiamy kod
if __name__ == '__main__':
    # Dla n = 10000
    start_time = perf_counter()
    quicksort(insert_random(10000), 0, 9999)
    end_time = perf_counter()
    print(f"Czas sortowania 10000 losowych elementów: {end_time - start_time:.6f} sekund\n")

    start_time = perf_counter()
    quicksort(insert_ascending(10000), 0, 9999)
    end_time = perf_counter()
    print(f"Czas sortowania 10000 posortowanych rosnąco elementów: {end_time - start_time:.6f} sekund\n")

    start_time = perf_counter()
    quicksort(insert_descending(10000), 0, 9999)
    end_time = perf_counter()
    print(f"Czas sortowania 10000 posortowanych malejąco elementów: {end_time - start_time:.6f} sekund\n")

    # Dla n = 50000
    start_time = perf_counter()
    quicksort(insert_random(50000), 0, 49999)
    end_time = perf_counter()
    print(f"Czas sortowania 50000 losowych elementów: {end_time - start_time:.6f} sekund\n")

    start_time = perf_counter()
    quicksort(insert_ascending(50000), 0, 49999)
    end_time = perf_counter()
    print(f"Czas sortowania 50000 posortowanych rosnąco elementów: {end_time - start_time:.6f} sekund\n")

    start_time = perf_counter()
    quicksort(insert_descending(50000), 0, 49999)
    end_time = perf_counter()
    print(f"Czas sortowania 50000 posortowanych malejąco elementów: {end_time - start_time:.6f} sekund\n")

    # Dla n = 100000
    start_time = perf_counter()
    quicksort(insert_random(100000), 0, 99999)
    end_time = perf_counter()
    print(f"Czas sortowania 100000 losowych elementów: {end_time - start_time:.6f} sekund\n")

    start_time = perf_counter()
    quicksort(insert_ascending(100000), 0, 99999)
    end_time = perf_counter()
    print(f"Czas sortowania 100000 posortowanych rosnąco elementów: {end_time - start_time:.6f} sekund\n")

    start_time = perf_counter()
    quicksort(insert_descending(100000), 0, 99999)
    end_time = perf_counter()
    print(f"Czas sortowania 100000 posortowanych malejąco elementów: {end_time - start_time:.6f} sekund\n")

# Output z losowym pivotem
# Czas sortowania 10000 losowych elementów: 0.013803 sekund
#
# Czas sortowania 10000 posortowanych rosnąco elementów: 0.013615 sekund
#
# Czas sortowania 10000 posortowanych malejąco elementów: 0.011224 sekund
#
# Czas sortowania 50000 losowych elementów: 0.080077 sekund
#
# Czas sortowania 50000 posortowanych rosnąco elementów: 0.060578 sekund
#
# Czas sortowania 50000 posortowanych malejąco elementów: 0.061844 sekund
#
# Czas sortowania 100000 losowych elementów: 0.162096 sekund
#
# Czas sortowania 100000 posortowanych rosnąco elementów: 0.132622 sekund
#
# Czas sortowania 100000 posortowanych malejąco elementów: 0.131429 sekund

# Output bez losowego pivota:
# Czas sortowania 10000 losowych elementów: 0.015897 sekund
#
# Czas sortowania 10000 posortowanych rosnąco elementów: 3.222383 sekund
#
# Czas sortowania 10000 posortowanych malejąco elementów: 2.385617 sekund
#
# Czas sortowania 50000 losowych elementów: 0.094743 sekund
#
# Czas sortowania 50000 posortowanych rosnąco elementów: 77.985035 sekund
#
# Czas sortowania 50000 posortowanych malejąco elementów: 53.643582 sekund
#
# Czas sortowania 100000 losowych elementów: 0.129958 sekund
#
# Czas sortowania 100000 posortowanych rosnąco elementów: 312.374934 sekund
#
# Czas sortowania 100000 posortowanych malejąco elementów: 220.148228 sekund
