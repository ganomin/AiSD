from linked_list import LinkedList

if __name__ == '__main__':
    l = LinkedList()

    # Wstawiamy elementy [10, 20, 30, 40]
    l.list_insert(10)
    l.list_insert(20)
    l.list_insert(30)
    l.list_insert(40)
    l.list_print()

    # Znajdywanie elementów
    search_value = 20
    result_node = l.list_search(search_value)
    if result_node is not None:
        print(f"Znaleziono węzeł {result_node.value}")
    else:
        print(f"Nie znaleziono węzła o wartości {search_value}")

    # Znajdywanie nieistniejącego elementu
    search_value = 50
    result_node = l.list_search(search_value)
    if result_node is not None:
        print(f"Znaleziono węzeł {result_node.value}")
    else:
        print(f"Nie znaleziono węzła o wartości {search_value}")

    # Usuwanie elementów
    l.list_delete(30)
    l.list_delete(50)
    l.list_print()

    # Użycie funkcji top()
    l.top()
    l.list_print()
    l.top()
    l.list_print()
    l.top()
    l.list_print()
