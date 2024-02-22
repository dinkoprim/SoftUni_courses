def coordinates_validator(x, y, size):
    valid_range = range(size)
    if x not in valid_range or y not in valid_range:
        return False
    return True


def actions(command, value, x, y):
    if command == 'Add':
        matrix[x][y] += value
    elif command == 'Subtract':
        matrix[x][y] -= value


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

input_line = input().split()
while input_line[0] != 'END':
    cmd = input_line[0]
    x, y, value = map(int, input_line[1:])

    if coordinates_validator(x, y, rows):
        actions(cmd, value, x, y)
    else:
        print(f'Invalid coordinates')

    input_line = input().split()

[print(*row) for row in matrix]