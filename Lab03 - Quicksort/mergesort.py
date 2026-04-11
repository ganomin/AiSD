# Zadanie 3.C
def mergesort(A):
    """ Implementacja bazuje na pseudokodzie z wykładu.
        Złożoność O(n * log n) """

    # Warunek rekurencyjny
    if len(A) <= 1:
        return A

    # Wyznacz środek tablicy
    mid = len(A) // 2

    # Podziel tablicę na lewą i prawą stronę i posortuj
    left = mergesort(A[:mid])
    right = mergesort(A[mid:])

    # Połącz posortowane połowy ze sobą i zwróć wynik
    return merge(left, right)


def merge(left, right):
    """ Implementacja bazuje na pseudokodzie z wykładu.
        Złożoność O(n) """

    # Zmienne pomocnicze
    result = []
    i, j = 0, 0

    # Przechodzimy po obu tablicach jednocześnie i dodajemy rosnąco posortowane liczby do wyniku
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Po zakończeniu pętli while, w którejś z list mogły pozostać jakieś dokumenty
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Uruchamiamy kod
if __name__ == '__main__':
    list_of_numbers = []

    with open('input_data.txt') as file:
        for line in file:
            list_of_numbers.append(int(line))

    print("Przed mergesort:", list_of_numbers)
    print("Po mergesort:", mergesort(list_of_numbers))
