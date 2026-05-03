def get_input_data(input_file, limit):
    input_data = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file):
            if line_number >= limit:
                break
            input_data.append(line.strip('\n'))

    return input_data


def h1(input_data, m):
    hash_table = []

    for _ in range(m):
        hash_table.append([])

    for word in input_data:
        ascii_value = sum(ord(c) for c in word) % m
        hash_table[ascii_value].append(word)

    return hash_table


def h2(input_data, m):
    hash_table = []

    for _ in range(m):
        hash_table.append([])

    for word in input_data:
        hash_value = 0
        char_position = 0

        for char in word:
            hash_value += ord(char) * 97 ** char_position
            char_position += 1

        hash_table[hash_value % m].append(word)


    return hash_table


def count_empty_elements(output):
    return sum(1 for lst in output if not lst)


def get_longest_list(output):
    return max(len(lst) for lst in output)


def get_non_empty_list_lengths(output):
    return [len(lst) for lst in output if lst]


def avg_list_length(output):
    return sum(get_non_empty_list_lengths(output)) / len(get_non_empty_list_lengths(output)) if get_non_empty_list_lengths(output) else 0


def run_experiment():
    input_file = "pl.txt"
    data_size = 5000
    m_sizes = [839, 1667, 2503]

    print(f"{'m':<4} | {'funkcja haszująca':<17} | {'liczba pustych list':<19} | {'maks. długość listy':<19} | {'średnia długość niepustych list'}")
    print("-" * 103)

    for m in m_sizes:
        h1_output = h1(get_input_data(input_file, data_size), m)
        h2_output = h2(get_input_data(input_file, data_size), m)

        h1_count_empty_elements = count_empty_elements(h1_output)
        h2_count_empty_elements = count_empty_elements(h2_output)

        h1_get_longest_list = get_longest_list(h1_output)
        h2_get_longest_list = get_longest_list(h2_output)

        h1_avg_list_length = avg_list_length(h1_output)
        h2_avg_list_length = avg_list_length(h2_output)

        print(f"{m:<4} | {"h1":<17} | {h1_count_empty_elements:<19} | {h1_get_longest_list:<19} | {h1_avg_list_length:.2f}")
        print(f"{m:<4} | {"h2":<17} | {h2_count_empty_elements:<19} | {h2_get_longest_list:<19} | {h2_avg_list_length:.2f}")
        print("-" * 103)


if __name__ == '__main__':
    run_experiment()
