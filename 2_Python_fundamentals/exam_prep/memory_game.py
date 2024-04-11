def check_if_match(idx_1, idx_2, sequence, turns):
    if valid_index(idx_1, idx_2, sequence):
        item1, item2 = sequence[idx_1], sequence[idx_2]

        if item1 == item2:
            print(f"Congrats! You have found matching elements - {item1}!")
            remove_match(idx_1, idx_2, sequence)

        else:
            print(f"Try again!")

    else:
        print("Invalid input! Adding additional elements to the board")
        adding_additional_elements(turns, sequence)


def valid_index(idx_1, idx_2, sequence):
    if not 0 <= idx_1 < len(sequence) or not 0 <= idx_2 < len(sequence) or idx_1 == idx_2:
        return False
    return True


def adding_additional_elements(turns, sequence):
    mid_idx = len(sequence) // 2
    for _ in range(2):
        sequence.insert(mid_idx, f'-{turns}a')


def remove_match(idx_1, idx_2, sequence):
    sorted_indices = list(sorted([idx_1, idx_2], reverse=True))
    for idx in sorted_indices:
        del sequence[idx]


def main():
    sequence = input().split()
    attempts = 0

    while sequence:
        pair_input = input()
        if pair_input == 'end':
            break

        attempts += 1
        idx1, idx2 = [int(x) for x in pair_input.split()]
        check_if_match(idx1, idx2, sequence, attempts)

    if sequence:
        return print(f"Sorry you lose :(\n{' '.join(str(x) for x in sequence)}")

    return print(f"You have won in {attempts} turns!")


if __name__ == "__main__":
    main()