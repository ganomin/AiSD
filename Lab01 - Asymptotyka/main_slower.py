# Bubble sort
def bubble_sort(bubble_input_data):
    # "Improved Bubble Sort algorithm" from: https://www.w3schools.com/python/python_dsa_bubblesort.asp
    list_length = len(bubble_input_data)

    for i in range(list_length - 1):
        swapped = False

        for j in range(list_length - i - 1):
            if bubble_input_data[j] > bubble_input_data[j + 1]:
                bubble_input_data[j], bubble_input_data[j + 1] = bubble_input_data[j + 1], bubble_input_data[j]
                swapped = True

            # If we didn't swap any numbers, there's no need to do more iterations.
            if not swapped:
                continue

    return bubble_input_data


# Main algorithm
def is_element_half_list(algorithm_input_data, x):
    print(algorithm_input_data)
    # How long is the input list?
    list_length = len(algorithm_input_data)

    # Is our list even? Is middle element x? Divide our list in half.
    if list_length % 2 == 0:
        if algorithm_input_data[list_length // 2 - 1] != x:  # Is middle-left element x?
            return False
        if algorithm_input_data[list_length // 2] != x:  # Is middle-right element x?
            return False

        list_left = algorithm_input_data[:list_length // 2]
        list_right = algorithm_input_data[list_length // 2:]

        number_of_occurrences = 0  # No middle 'x'.

    else:
        if not algorithm_input_data[list_length // 2 - 1] == x:
            return False

        list_left = algorithm_input_data[:list_length // 2]
        list_right = algorithm_input_data[list_length // 2 + 1:]

        number_of_occurrences = 1  # Preemptively count middle 'x'.

    # Count occurrences of 'x'.
    for number in list_left[::-1]:
        if number is x:
            number_of_occurrences += 1
        else:
            break

    for number in list_right:
        if number is x:
            number_of_occurrences += 1
        else:
            break

    # Final check
    if number_of_occurrences >= list_length / 2:
        return True
    else:
        return False


# Main runner
if __name__ == '__main__':
    # Gather user input
    print("Wpisz liczbę, którą chcesz wprowadzić do programu. Enter zaakceptuje dane, lub przejdzie dalej.")
    user_input_data = []

    while True:
        user_input = input()
        if not user_input:
            break
        user_input_data.append(int(user_input))

    # Ask user for x
    print("Wpisz szukane 'x'")
    x = int(input())

    # Run algorithm
    print("Wynik:", is_element_half_list(bubble_sort(user_input_data), x))
