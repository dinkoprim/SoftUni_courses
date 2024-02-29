n = int(input())


def print_row(size, row):
    print(f"{' ' * (size - row)}{'* ' * row}")


def print_rhomb_upper(size):
    for row in range(1, size+1):
        print_row(size, row)


def print_rhomb_bottom(size):
    for row in range(size-1, 0, -1):
        print_row(size, row)


print_rhomb_upper(n)
print_rhomb_bottom(n)
