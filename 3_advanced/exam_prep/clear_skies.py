N = int(input())

matrix = []
position = (0, 0)
r, c = position
armor = 300
enemy_planes = 0

for row_index in range(N):
    line = list(input())

    if 'J' in line:
        position = (row_index, line.index('J'))
        r, c = position

    if 'E' in line:
        enemy_planes += line.count('E')

    matrix.append(line)

directions_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def move_jet(position, direction):
    step = directions_mapper[direction]
    next_position = tuple(step[i] + position[i] for i in range(2))

    return next_position


while True:
    command = str(input())
    matrix[r][c] = '-'

    r, c = move_jet(position, command)
    position = (r, c)

    if matrix[r][c] == 'E':
        enemy_planes -= 1

        if not enemy_planes:
            print("Mission accomplished, you neutralized the aerial threat!")
            matrix[r][c] = 'J'
            break
        armor -= 100

        if armor <= 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
            matrix[r][c] = 'J'
            break
            
    elif matrix[r][c] == 'R':
        armor = 300

    matrix[r][c] = 'J'

[print(''.join(row)) for row in matrix]
