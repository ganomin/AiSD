class Node:
    """ Klasa pomocnicza węzła przechowująca wartości elementów i wskaźniki
        Kod bazuje na kodzie z wykładu """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
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

    # szukaj(x)
    def list_search(self, x):
        """ Funkcja zwraca węzeł listy o wartości równej `x`, o ile taka liczba znajduje się na liście,
            a w przeciwnym wypadku zwraca None
            Złożoność: O(n)
            Kod bazuje na kodzie z wykładu """

        current = self.head
        while current is not None and current.value != x:
            current = current.next

        return current

    # usuń(x)
    def list_delete(self, x):
        """ Funkcja usuwa z listy pierwszy napotkany węzeł o wartości `x`
            Złożoność: O(n)
            Kod bazuje na kodzie z wykładu """

        # Wywołujemy funkcję `list_search()`, by sprawdzić, czy dany element w ogóle istnieje
        node = self.list_search(x)
        if node is None:
            return

        # Jeśli węzeł miał poprzednika, to wskaźnik poprzednika zaczyna wskazywać na element za usuwanym węzłem
        if node.prev is not None:
            node.prev.next = node.next
        else:
            # Jeśli węzeł nie miał poprzednika, `head` staję się jego następnikiem
            self.head = node.next

        # Jeśli węzeł miał następnika, przepinamy jego wskaźnik `prev` na poprzednika usuniętego węzła
        if node.next is not None:
            node.next.prev = node.prev

    # top()
    def top(self):
        """ Funkcja usuwa pierwszy węzeł z listy
            Złożoność: O(1) """

        if self.head is not None:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
