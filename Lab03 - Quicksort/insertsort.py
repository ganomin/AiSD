# Zadanie 3.D
from random import randint, uniform
from time import perf_counter


# Algorytm Insert Sort
def insertsort(A, low, high):
    for i in range(low + 1, high + 1):
        key = A[i]
        j = i - 1
        while j >= low and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


# Algorytm Quicksort
def quicksort(A, low, high, M):
    # Przełączenie się na Insert Sort dla małych N
    if high - low + 1 <= M:
        insertsort(A, low, high)
        return

    # Klasyczny Quick Sort
    if low < high:
        p = partition(A, low, high)
        quicksort(A, low, p - 1, M)
        quicksort(A, p + 1, high, M)


# Algorytm na podział tablicy
def partition(A, low, high):
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
    for _ in range(n):
        list_of_numbers.append(uniform(0.0, 1000.0))
    return list_of_numbers


# Uruchamiamy kod
if __name__ == '__main__':
    sizes_of_n = [1000, 10000, 100000, 1000000]
    sizes_of_m = [0, 10, 100, 1000]

    for n in sizes_of_n:
        print(f"Sortowanie dla N = {n} elementów")

        # Generujemy testową tablicę
        input_data = insert_random(n)

        for m in sizes_of_m:
            data_to_sort = input_data.copy()

            start_time = perf_counter()
            quicksort(data_to_sort, 0, len(data_to_sort) - 1, m)
            end_time = perf_counter()

            print(f"Parametr M = {m:<4} | Czas: {end_time - start_time:.5f} s")

        print("\n")
