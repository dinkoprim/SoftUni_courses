hood = []
position = (0, 0)

rows, cols = [int(x) for x in input().split()]

for row in range(rows):
    line = list(input())
    if 'B' in line:
        position = (row, line.index('B'))
        x, y = position
    hood.append(line)

r, c = position
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    if hood[r][c] == 'A':
        hood[r][c] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

    cmd = input()

    step = directions[cmd]
    next_position = tuple(step[i] + position[i] for i in range(2))

    if next_position[0] not in range(rows) or next_position[1] not in range(cols):
        print("The delivery is late. Order is canceled.")
        hood[x][y] = ' '
        break
    elif hood[next_position[0]][next_position[1]] == '*':
        continue

    r, c = next_position
    position = (r, c)

    if hood[r][c] != '-':
        if hood[r][c] == 'P':
            print("Pizza is collected. 10 minutes for delivery.")
            hood[r][c] = 'R'
    else:
        hood[r][c] = '.'

[print(''.join(r)) for r in hood]