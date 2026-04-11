import math

# Bubble sort – O(n^2)
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


# We need to find first and last index of 'x' in our already sorted list.
# Adapted from: https://www.geeksforgeeks.org/dsa/find-first-and-last-positions-of-an-element-in-a-sorted-array/
def find_first_index(list_to_search, x):  # Find first index – O(log n)
    length = len(list_to_search)
    lowest = 0
    highest = length - 1
    last_occurrence = -1

    while lowest <= highest:
        middle = (lowest + highest) // 2

        # Is 'x' middle element?
        if x == list_to_search[middle]:
            last_occurrence = middle
            highest = middle - 1
        # Is 'x' smaller than middle element?
        elif x < list_to_search[middle]:
            highest = middle - 1
        # 'x' must be bigger than middle element.
        else:
            lowest = middle + 1

    return last_occurrence


def is_element_half_list(algorithm_input_data, x):
    # Is middle element/s x?
    if len(algorithm_input_data) % 2 == 0:
        if algorithm_input_data[len(algorithm_input_data) // 2 - 1] != x:  # Is middle-left element x?
            return False
        if algorithm_input_data[len(algorithm_input_data) // 2] != x:  # Is middle-right element x?
            return False
    else:
        if not algorithm_input_data[len(algorithm_input_data) // 2 - 1] == x:
            return False

    # Find first occurrence
    first_index = find_first_index(algorithm_input_data, x)

    # Now we need to check if "opposite" element of 'x' is still 'x'.
    # If so, we have certainty that 'x' takes place for more than n / 2 of the list.
    if algorithm_input_data[math.ceil(first_index + len(algorithm_input_data) / 2 - 1)] == x:
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
    print(is_element_half_list(bubble_sort(user_input_data), x))
