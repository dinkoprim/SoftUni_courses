size = int(input())
area = []
fish_collected = 0
quota = -20
start_row, start_col = 0, 0

for i in range(size):
    row = input()
    if 'S' in row:
        start_row, start_col = i, row.index('S')
    area.append([int(x) if str(x).isdigit() else x for x in row])

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

area[start_row][start_col] = '-'
r, c = start_row, start_col

cmd = input()
while cmd != 'collect the nets':

    step = directions_mapper[cmd]
    r, c = step[0] + r, step[1] + c

    r = (r + size) % size
    c = (c + size) % size

    if area[r][c] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{r},{c}]")
        raise SystemExit
    elif area[r][c] != '-':
        fish_collected += area[r][c]
        quota += area[r][c]
        area[r][c] = '-'

    cmd = input()

area[r][c] = 'S'

if quota >= 0:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {abs(quota)} tons of fish more.")

if fish_collected:
    print(f"Amount of fish caught: {fish_collected} tons.")

for row in area:
    print(''.join(str(x) for x in row))
