import random


# Wprowadzenie danych
def get_input(file, limit):
    input_data = []

    with open(file, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f):
            if line_number >= limit:
                break

            parts = line.strip().split()

            value = int(parts[0])
            last_name = parts[1]

            input_data.append((last_name, value))

    return input_data


# Funkcja haszująca
def compute_hash(key, m):
    return sum(ord(char) for char in key) % m


# Wstawianie
def table_insert(hash_table, key, value, m):
    hash_value = compute_hash(key, m)
    attempts = 0

    for i in range(m):
        attempts += 1
        index = (hash_value + i) % m

        if hash_table[index] is None or hash_table[index] == 'DEL':
            hash_table[index] = (key, value)

            return attempts

    return attempts


# Wyszukanie
def table_search(hash_table, key, m):
    hash_value = compute_hash(key, m)
    attempts = 0

    for i in range(m):
        attempts += 1
        index = (hash_value + i) % m

        if hash_table[index] is None:
            return None, attempts

        if hash_table[index] != 'DEL' and hash_table[index][0] == key:
            return hash_table[index][1], attempts

    return None, attempts


# Usuwanie
def table_delete(hash_table, key, m):
    hash_value = compute_hash(key, m)

    for i in range(m):
        index = (hash_value + i) % m

        if hash_table[index] is None:
            return False

        if hash_table[index] != 'DEL' and hash_table[index][0] == key:
            hash_table[index] = 'DEL'

            return True

    return False


def first_experiment():
    m = 3500
    alpha_values = [0.25, 0.50, 0.75, 0.90]
    input_data = get_input('nazwiskaASCII.txt', m)
    unexisting_keys = [f"NieistniejącyKlucz{i}" for i in range(m)]

    print(f"{'α':4} | {'średnia liczba prób (sukces)':18} | {'średnia liczba prób (porażka)':20} | {'max prób'}")
    print("-" * 78)

    for alpha in alpha_values:
        n = int(m * alpha)
        data_to_hash = input_data[:n]
        hash_table = [None] * m

        for key, val in data_to_hash:
            table_insert(hash_table, key, val, m)

        success_attempts_total = 0
        success_attempts_max = 0
        for key, _ in data_to_hash:
            _, attempts = table_search(hash_table, key, m)
            success_attempts_total += attempts
            success_attempts_max = max(success_attempts_max, attempts)

        fail_attempts_total = 0
        fail_attempts_max = 0
        for key in unexisting_keys:
            _, attempts = table_search(hash_table, key, m)
            fail_attempts_total += attempts
            fail_attempts_max = max(fail_attempts_max, attempts)

        avg_success = success_attempts_total / n
        avg_fail = fail_attempts_total / m

        max_all = max(success_attempts_max, fail_attempts_max)

        print(f"{alpha:<1.2f} | {avg_success:28.2f} | {avg_fail:29.2f} | {max_all}")


def second_experiment():
    m = 3500
    alpha = 0.75
    input_data = get_input('nazwiskaASCII.txt', m)
    unexisting_keys = [f"NieistniejącyKlucz{i}" for i in range(m)]

    n = int(m * alpha)
    data_to_hash = input_data[:n]
    hash_table = [None] * m

    for key, val in data_to_hash:
        table_insert(hash_table, key, val, m)

    num_to_delete = int(n * 0.30)
    inserted_keys = []

    for key, _ in data_to_hash:
        inserted_keys.append(key)

    keys_to_delete = list(random.sample(inserted_keys, num_to_delete))

    for key in keys_to_delete:
        table_delete(hash_table, key, m)

    remaining_keys = []
    for key in inserted_keys:
        if key not in keys_to_delete:
            remaining_keys.append(key)

    success_attempts_total = 0
    success_attempts_max = 0
    for key in remaining_keys:
        _, attempts = table_search(hash_table, key, m)
        success_attempts_total += attempts
        success_attempts_max = max(success_attempts_max, attempts)

    fail_attempts_total = 0
    fail_attempts_max = 0
    for key in unexisting_keys:
        _, attempts = table_search(hash_table, key, m)
        fail_attempts_total += attempts
        fail_attempts_max = max(fail_attempts_max, attempts)

    avg_success = success_attempts_total / len(remaining_keys)
    avg_fail = fail_attempts_total / m
    max_all = max(success_attempts_max, fail_attempts_max)

    print(f"{'α':4} | {'średnia liczba prób (sukces)':18} | {'średnia liczba prób (porażka)':20} | {'max prób'}")
    print("-" * 78)

    new_alpha = len(remaining_keys) / m

    print(f"{new_alpha:<1.2f} | {avg_success:28.2f} | {avg_fail:29.2f} | {max_all}")


if __name__ == '__main__':
    print("\n" + "Eksperyment 1:")
    first_experiment()

    print("\n" + "Eksperyment 2:")
    second_experiment()
