rows, cols = [int(x) for x in input().split()]
matrix = []
position = (0, 0)
r, c = position
moves = 0
touched_players = 0

for row_index in range(rows):
    line = input().split()
    if 'B' in line:
        position = (row_index, line.index('B'))
        r, c = position
    matrix.append(line)


def move_player(position, direction):
    step = directions_mapper[direction]
    next_position = tuple(step[i] + position[i] for i in range(2))

    if next_position[0] not in range(rows) or next_position[1] not in range(cols):
        return None
    elif matrix[next_position[0]][next_position[1]] == 'O':
        return None

    return next_position


directions_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

cmd = input()
while cmd != 'Finish' and touched_players < 3:
    matrix[r][c] = '-'

    if move_player(position, cmd):
        moves += 1
        r, c = move_player(position, cmd)
        position = (r, c)

        if matrix[r][c] == 'P':
            touched_players += 1

        matrix[r][c] = 'B'

    cmd = input()

print('Game over!')
print(f"Touched opponents: {touched_players} Moves made: {moves}")