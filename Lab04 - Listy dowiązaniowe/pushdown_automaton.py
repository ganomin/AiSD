class Node:  # Bez zmian
    """ Klasa pomocnicza węzła przechowująca wartości elementów i wskaźniki
        Kod bazuje na kodzie z wykładu """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:  # Bez zmian
    """ Klasa reprezentująca listę dowiązaną dwukierunkową niecykliczną """

    def __init__(self):
        # Deklarujemy pustą tablicę (bez wartownika)
        self.head = None

    # wstaw(x)
    def list_insert(self, x):
        """ Funkcja wstawia liczbę `x` na początek listy
            Złożoność: O(1)
            Lekko zmodyfikowany kod z wykładu """

        # Tworzymy nowy węzeł i ustawiamy wskaźnik `next` na wcześniejszą głowę listy
        new_node = Node(x)
        new_node.next = self.head

        # Jeśli lista nie była pusta, wskaźnik `prev` dotychczasowej głowy będzie wskazywał na nowy węzeł
        if self.head is not None:
            self.head.prev = new_node

        # Przestawiamy `head` na nowy węzeł
        self.head = new_node

    # drukuj()
    def list_print(self):
        """ Funkcja wypisuje po kolei wszystkie elementy listy
            Lekko zmodyfikowany kod z wykładu
            Złożoność: O(n) """

        if self.head is None:
            print("Lista dowiązana pusta")

        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next

        print()

    # top()
    def top(self):
        """ Funkcja usuwa pierwszy węzeł z listy
            Złożoność: O(1) """

        if self.head is not None:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None


def simulate(word):
    """ Funkcja symuluje automat ze stosem rozpoznający konkretny język """

    # Generujemy nasz stos
    stack = LinkedList()
    stack.list_insert('Z')
    current_state = 'q_a'

    # Iterujemy po każdym symbolu słowa
    for symbol in word:
        # Wypisz aktualny stan automatu
        # stack.list_print()

        if current_state == 'q_a':
            if symbol == 'a':
                stack.list_insert('a')
            elif symbol == 'c':
                current_state = 'q_c1'
            else:
                return "NIE"

        elif current_state == 'q_c1':
            if symbol == 'c':
                current_state = 'q_c2'
            else:
                return "NIE"

        elif current_state == 'q_c2':
            if symbol == 'c':
                current_state = 'q_b_pop'
            else:
                return "NIE"

        elif current_state == 'q_b_pop':
            if symbol == 'b':
                if stack.head is not None and stack.head.value == 'a':
                    stack.top()
                elif stack.head is not None and stack.head.value == 'Z':
                    current_state = 'q_b_accept'
                else:
                    return "NIE"
            else:
                return "NIE"

        elif current_state == 'q_b_accept':
            if symbol == 'b':
                pass
            else:
                return "NIE"

    if current_state == 'q_b_accept':
        return "TAK"
    else:
        return "NIE"


if __name__ == '__main__':
    words = ["aacccbbb", "cccb", "acccb", "abcccb"]

    for w in words:
        print(f"Słowo: '{w}' daje wynik: {simulate(w)}")
