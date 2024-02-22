sequence = input().split(' ')


def sorting(some_integers):
    result = list(map(int, some_integers))
    return sorted(result)


print(sorting(sequence))
