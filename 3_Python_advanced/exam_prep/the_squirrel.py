from collections import deque


def move_squirrel(position, direction):
    step = directions[direction]
    next_position = tuple(step[i] + position[i] for i in range(2))

    if next_position[0] not in range(size) or next_position[1] not in range(size):
        print("The squirrel is out of the field.")
        return None

    return next_position


collected_hazelnuts = 0
size = int(input())
commands = deque(input().split(', '))
matrix = []
position = ()
r, c = (0, 0)

for row_index in range(size):
    line = list(input())
    if 's' in line:
        position = (row_index, line.index('s'))
        r, c = position
    matrix.append(line)

matrix[r][c] = '*'
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while commands:
    cmd = commands.popleft()
    next_position = move_squirrel(position, cmd)
    if next_position is None:
        break

    r, c = next_position
    position = (r, c)

    if matrix[r][c] != '*':
        if matrix[r][c] == 't':
            print("Unfortunately, the squirrel stepped on a trap...")
            break

        elif matrix[r][c] == 'h':
            collected_hazelnuts += 1

            if collected_hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")
                break
            matrix[r][c] = '*'

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")
