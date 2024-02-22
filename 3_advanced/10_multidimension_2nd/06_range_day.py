matrix = []
size = 5
shooter_pos = []
targets_hit_pos = []
targets_hit = 0
targets = 0

for row_i in range(size):
    matrix.append(input().split())
    if 'A' in matrix[row_i]:
        shooter_pos = [row_i, matrix[row_i].index('A')]

    targets += matrix[row_i].count('x')

commands_count = int(input())

heading = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0),
}

for _ in range(commands_count):
    command = input().split()
    action, direction = command[0], command[1]

    if action == 'move':
        steps = int(command[2])
        row = shooter_pos[0] + steps * heading[direction][0]
        col = shooter_pos[1] + steps * heading[direction][1]

        if 0 <= row < size and 0 <= col < size and matrix[row][col] == '.':
            shooter_pos = [row, col]

    elif action == 'shoot':
        bullet_pos = shooter_pos.copy()
        row, col = bullet_pos

        while 0 <= row < size and 0 <= col < size:
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                targets_hit_pos.append([row, col])
                targets_hit += 1
                break
            else:
                row += heading[direction][0]
                col += heading[direction][1]

    if targets_hit == targets:
        print(f'Training completed! All {targets} targets hit.')
        for pos in targets_hit_pos:
            print(pos)
        break

if targets_hit < targets:
    print(f'Training not completed! {targets - targets_hit} targets left.')
    for pos in targets_hit_pos:
        print(pos)
