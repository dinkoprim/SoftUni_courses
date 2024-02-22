from pyfiglet import figlet_format


class FullColumnError(Exception):
    pass


class InvalidColumnChoice(Exception):
    pass


ROWS, COLS = 6, 7


def board_print():
    for row in board:
        print(" " * 3, end="")
        print(f"| {' | '.join(str(x) if x != 0 else ' ' for x in row)} |")
    print()


def valid_column(choice):
    if 1 <= choice <= COLS:
        return True
    raise InvalidColumnChoice('player choice out of range')


def get_free_row(col_idx, board):
    for row_idx in range(ROWS-1, -1, -1):
        if board[row_idx][col_idx] == 0:
            return row_idx
    else:
        raise FullColumnError('column is full')


DIRECTION_MAP = {
    'left': (0, -1),
    'up': (-1, 0),
    'prime_dia_up': (-1, -1),
    'other_dia_up': (-1, 1),
}


def travel_direction(coordinates, element, curr_row, curr_col, board):
    counter = 0
    row_direction, col_direction = coordinates

    for i in range(1, 4):
        next_element_row_idx = curr_row + row_direction * i
        next_element_col_idx = curr_col + col_direction * i
        try:
            if board[next_element_row_idx][next_element_col_idx] == element:
                counter += 1
            else:
                return counter
        except IndexError:
            return counter
    return counter


def travel_opposite_direction(coordinates, element, curr_row, curr_col, board):
    counter = 0
    row_direction, col_direction = coordinates

    for i in range(1, 4):
        next_element_row_idx = curr_row - row_direction * i
        next_element_col_idx = curr_col - col_direction * i
        try:
            if board[next_element_row_idx][next_element_col_idx] == element:
                counter += 1
            else:
                return counter
        except IndexError:
            return counter
    return counter


def is_winner(curr_row, curr_col, board):
    for direction, coordinates in DIRECTION_MAP.items():
        searched_element = board[curr_row][curr_col]
        travel_direction_counter = travel_direction(coordinates, searched_element, curr_row, curr_col,  board)
        travel_opposite_direction_counter = (
            travel_opposite_direction(coordinates, searched_element, curr_row, curr_col, board))

        if travel_direction_counter + travel_opposite_direction_counter + 1 >= 4:
            return True
    else:
        return False


def board_is_full(board):
    if not board[0].count(0):
        return True
    return False


def valid_symbol(symbol):
    if not symbol or symbol == ' ':
        print('Invalid symbol')
        return False

    elif len(symbol) > 1:
        print('Invalid symbol: only one symbol allowed')
        return False
    return True


def players_symbols():
    while True:
        player_1 = input('Player 1, enter your symbol: ')
        if valid_symbol(player_1):
            break
        else:
            print('Please try again.')

    while True:
        player_2 = input('Player 2, enter your symbol: ')
        if valid_symbol(player_2):
            print()
            break
        else:
            print('Please try again.')
    print(f'Player 1 plays with {player_1}\nPlayer 2 plays with {player_2}\n\nLets begin!')
    return player_1, player_2


print(figlet_format('Connect 4',), end='')

player_1, player_2 = players_symbols()

print(' ==================================')
print('The first Player to CONNECT 4 wins!')
print(' ==================================')
board = [[0]*COLS for row in range(ROWS)]
board_print()
turn = 1


while True:
    player = player_2 if turn % 2 == 0 else player_1

    try:
        column_choice = int(input(f'    Player {player} choose a column: '))
        valid_column(column_choice)

        column_idx = column_choice - 1
        row_idx = get_free_row(column_idx, board)
        board[row_idx][column_idx] = player

        if is_winner(row_idx, column_idx, board):
            break
        if board_is_full(board):
            print('Board is full, nobody wins')
            exit(0)

    except FullColumnError:
        print('This column is full, select another.')
        continue
    except (InvalidColumnChoice, ValueError):
        print(f'This column choice is invalid, please select a number between 1 and {COLS}')
        continue

    board_print()
    turn += 1

board_print()
print(f'WINNER Player {player} !')
