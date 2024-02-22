from collections import deque


def check_if_winner():
    player_name, player_symbol = players[0].values()

    prime_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])
    row_win = any([all(el == player_symbol for el in row) for row in board])
    col_win = any([all([board[row][col] == player_symbol for row in range(SIZE)]) for col in range(SIZE)])

    if any([prime_diagonal_win, second_diagonal_win, row_win, col_win]):
        show_board()
        print(f'{player_name} is the WINNER')

        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0]['symbol']

    check_if_winner()
    show_board()

    if turns == SIZE**2:
        print('DRAW')
        raise SystemExit

    players.rotate()


def player_choice():
    global turns

    while True:
        try:
            position = int(input(f"{players[0]['name']} choose a free position [1 - {SIZE**2}]: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print_select_valid_position_msg()
            continue

        if 1 <= position <= SIZE**2 and board[row][col] == ' ':
            turns += 1
            place_symbol(row, col)
        else:
            print_select_valid_position_msg()


def print_select_valid_position_msg():
    print(f"{players[0]['name']} can't place there.")


def show_board():
    for r in board:
        print(" " * (SIZE + 1), end="")
        print(f"| {' | '.join(r)} |")


def print_game_state(first_turn=False):
    if first_turn:
        print('This is the numeration of the board:')
        show_board()
        print('Players choose an empty field by typing its number.')
        for r in range(SIZE):
            for c in range(SIZE):
                board[r][c] = ' '
    else:
        show_board()


def start():
    player_1_name = input('Player 1 please input your name: ')
    player_2_name = input('Player 2 please input your name: ')

    while True:
        player_1_symbol = input(f'{player_1_name} would you like to play with X or O ?: ').upper()
        if player_1_symbol not in ['X', 'O']:
            print(f'{player_1_name}Please select a valid symbol!')
        else:
            player_2_symbol = 'X' if player_1_symbol == 'O' else 'O'
            print(f'\n{player_1_name} plays with {player_1_symbol}  #  {player_2_name} plays with {player_2_symbol}')
            break

    players.append({'name': player_1_name, 'symbol': player_1_symbol})
    players.append({'name': player_2_name, 'symbol': player_2_symbol})

    print_game_state(first_turn=True)
    player_choice()


SIZE = 3
turns = 0
max_turns = SIZE ** 2

board = [[str(r+c) for c in range(SIZE)]for r in range(1, SIZE**2 + 1, SIZE)]

players = deque()
start()
