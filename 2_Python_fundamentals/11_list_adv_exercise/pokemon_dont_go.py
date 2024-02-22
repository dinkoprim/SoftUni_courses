def modify_pokemon_sequence(sequence, index):
    if not sequence:
        return 0

    if index < 0:
        removed_element = sequence[0]
        sequence.pop(0)
        sequence.insert(0, sequence[-1])
    elif index >= len(sequence):
        removed_element = sequence[-1]
        sequence.pop()
        sequence.append(sequence[0])
    else:
        removed_element = sequence[index]
        sequence.pop(index)

    for i in range(len(sequence)):
        if sequence[i] <= removed_element:
            sequence[i] += removed_element
        else:
            sequence[i] -= removed_element

    return removed_element


def pokemon_catcher(sequence):
    removed_elements = []

    while sequence:
        index = int(input())
        removed_element = modify_pokemon_sequence(sequence, index)
        removed_elements.append(removed_element)

    return sum(removed_elements)


sequence = [int(n) for n in input().split()]
print(pokemon_catcher(sequence))
