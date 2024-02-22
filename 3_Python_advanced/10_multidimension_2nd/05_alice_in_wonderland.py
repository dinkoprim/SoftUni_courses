size = int(input())

matrix = []
alice_position = []

tea_gathered = 0

move_commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row_i in range(size):
    matrix.append(input().split())
    if 'A' in matrix[row_i]:
        alice_position = [row_i, matrix[row_i].index('A')]
        matrix[row_i][matrix[row_i].index('A')] = '*'

while tea_gathered < 10:
    direction = input()

    row = alice_position[0] + move_commands[direction][0]
    col = alice_position[1] + move_commands[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_position = [row, col]
    token = matrix[row][col]
    matrix[row][col] = '*'

    if token == 'R':
        break

    if token.isdigit():
        tea_gathered += int(token)

if tea_gathered < 10:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

for row in matrix:
    print(*row)
