def find_bunny_row_col():
    for row_i in range(size):
        for col_i in range(size):
            if matrix[row_i][col_i] == 'B':
                return row_i, col_i


def bunny_can_move(x, y):
    if 0 <= x < size and 0 <= y < size:
        if matrix[x][y] != 'X':
            return True
    return False


size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

max_eggs = float('-inf')
best_path = []
best_direction = None

directions = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1),
}

row, col = find_bunny_row_col()

for heading, move in directions.items():
    new_row, new_col = move(row, col)
    path = []
    eggs_gathered = 0
    max_iterations = size * size

    while bunny_can_move(new_row, new_col) and max_iterations > 0:
        eggs_gathered += matrix[new_row][new_col]
        path.append([new_row, new_col])

        new_row, new_col = move(new_row, new_col)
        max_iterations -= 1

    if eggs_gathered >= max_eggs:
        max_eggs = eggs_gathered
        best_path = path
        best_direction = heading

print(best_direction)
[print(step) for step in best_path]
print(max_eggs)