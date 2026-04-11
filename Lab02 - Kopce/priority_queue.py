# Get the parent child of element i
def _parent(i):
    return (i - 1) // 2


# Get the left child of element i
def _left(i):
    return 2 * i + 1


# Get the right child of element i
def _right(i):
    return 2 * i + 2


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, key, value):
        """ Wstawienie nowej pary do kolejki.
            Złożoność: O(log n) """
        self.heap.append((key, value))
        self._bubble_up(len(self.heap) - 1)

    def minimum(self):
        """ Zwrócenie pary o najmniejszym kluczu, przy czym kolejka pozostaje bez zmian.
            Złożoność: O(1) """
        if not self.heap:
            return None

        return self.heap[0]

    def extract_min(self):
        """ Usunięcie i zwrócenie pary o najmniejszym kluczu.
            Złożoność: O(log n) """
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)

        return root

    def decrease_key(self, index, new_key):
        """ Zmiana wartości klucza elementu o zadanym indeksie index na mniejszy klucz new_key.
            Złożoność: O(log n) """
        self.heap[index] = (new_key, self.heap[index][1])
        self._bubble_up(index)

    # Used when adding new key
    def _bubble_up(self, i):
        while i > 0 and self.heap[_parent(i)][0] > self.heap[i][0]:
            p = _parent(i)
            if self.heap[p][0] > self.heap[i][0]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    # Used when removing
    def _bubble_down(self, i):
        smallest = i
        l, r = _left(i), _right(i)
        n = len(self.heap)

        if l < n and self.heap[l][0] < self.heap[smallest][0]:
            smallest = l
        if r < n and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r

        if not smallest == i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._bubble_down(smallest)


# Main runner
if __name__ == '__main__':
    pq = PriorityQueue()
    results = []

    pq.insert(ord('p'), 'p')
    pq.insert(ord('r'), 'r')
    pq.insert(ord('i'), 'i')
    pq.insert(ord('o'), 'o')
    results.append(pq.extract_min()[1])  # i
    pq.insert(ord('r'), 'r')
    results.append(pq.extract_min()[1])  # o
    results.append(pq.extract_min()[1])  # p
    pq.insert(ord('i'), 'i')
    results.append(pq.extract_min()[1])  # i
    pq.insert(ord('t'), 't')
    results.append(pq.extract_min()[1])  # r
    pq.insert(ord('y'), 'y')
    results.append(pq.extract_min()[1])  # r
    results.append(pq.extract_min()[1])  # t
    results.append(pq.extract_min()[1])  # y
    pq.insert(ord('q'), 'q')
    pq.insert(ord('u'), 'u')
    pq.insert(ord('e'), 'e')
    results.append(pq.extract_min()[1])  # e
    results.append(pq.extract_min()[1])  # q
    results.append(pq.extract_min()[1])  # u
    pq.insert(ord('u'), 'u')
    results.append(pq.extract_min()[1])  # u
    pq.insert(ord('e'), 'e')

    print(results)  # Wynik: [i, o, p, i, r, r, t, y, e, q, u, u]

# Źródła wykorzystane przy pisaniu/analizowaniu kodu
# https://www.geeksforgeeks.org/dsa/binary-heap/
# https://www.programiz.com/dsa/heap-data-structure
