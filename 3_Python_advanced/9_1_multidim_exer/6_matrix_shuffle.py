def is_valid_coordinates(coordinates):
    for coord in coordinates:
        if not coord.isdigit() or int(coord) < 0:
            return False
    return True


def command_validator(cmd, coordinates, rows, cols):
    if cmd != 'swap' or len(coordinates) != 4:
        return False

    if not is_valid_coordinates(coordinates):
        return False

    row1, col1, row2, col2 = map(int, coordinates)
    if not (row1 in range(rows) and col1 in range(cols) and row2 in range(rows) and col2 in range(cols)):
        return False

    return True


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

input_line = input().split()
while input_line[0] != 'END':
    cmd, *coords = input_line
    if command_validator(cmd, coords, rows, cols):
        row1, col1, row2, col2 = map(int, coords)
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(' '.join(row))
    else:
        print(f'Invalid input!')

    input_line = input().split()
