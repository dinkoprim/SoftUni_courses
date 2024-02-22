rows, columns = [int(x) for x in input().split(',')]

box = []
position = (0, 0)
cheese_count = 0

for r in range(rows):
    line = list(input())
    if 'M' in line:
        position = (r, line.index('M'))
    if 'C' in line:
        cheese_count += line.count('C')
    box.append(line)

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
r, c = position
box[r][c] = '*'

while True:
    cmd = input()

    if cmd == 'danger':
        print("Mouse will come back later!")
        box[r][c] = 'M'
        break

    step = directions[cmd]
    next_position = tuple(step[i] + position[i] for i in range(2))

    if next_position[0] not in range(rows) or next_position[1] not in range(columns):
        print("No more cheese for tonight!")
        box[r][c] = 'M'
        break

    elif box[next_position[0]][next_position[1]] == '@':
        continue

    r, c = next_position
    position = (r, c)

    if box[r][c] != '*':
        if box[r][c] == 'T':
            box[r][c] = 'M'
            print("Mouse is trapped!")
            break

        elif box[r][c] == 'C':
            cheese_count -= 1

            if cheese_count == 0:
                box[r][c] = 'M'
                print("Happy mouse! All the cheese is eaten, good night!")
                break

            box[r][c] = '*'

[print(''.join(r)) for r in box]
