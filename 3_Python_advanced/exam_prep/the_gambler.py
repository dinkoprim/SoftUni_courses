board_size = int(input())
board = []
position = []
pot = 100

for r in range(board_size):
    line = list(input())
    if 'G' in line:
        position = [r, line.index('G')]
    board.append(line)

r, c = position
board[r][c] = '-'
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

cmd = input()
while cmd != 'end':
    step = directions[cmd]
    r, c = r + step[0], c + step[1]

    if r not in range(board_size) or c not in range(board_size):
        print("Game over! You lost everything!")
        raise SystemExit

    if board[r][c] != '-':
        if board[r][c] == 'W':
            pot += 100
        elif board[r][c] == 'P':
            pot -= 200
            if pot <= 0:
                print("Game over! You lost everything!")
                raise SystemExit
        elif board[r][c] == 'J':
            pot += 100000
            print(f"You win the Jackpot!")
            board[r][c] = 'G'
            break
        board[r][c] = '-'

    cmd = input()

    if cmd == 'end':
        board[r][c] = 'G'

print(f"End of the game. Total amount: {pot}$")
for r in board:
    print(''.join(r))
