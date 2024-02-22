def could_attack(x, y, size):
    if x in range(size) and y in range(size):
        if matrix[x][y] == 'K':
            return True
    return False


board_size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input()] for _ in range(board_size)]

possible_positions = [-2, -1, 1, 2]
moves = [(x, y) for x in possible_positions for y in possible_positions if abs(x) != abs(y)]

# !
# moves = (
#     (-2, -1),
#     (-1, -2),
#     (1, -2),
#     (2, -1),
#     (2, 1),
#     (1, 2),
#     (-1, 2),
#     (-2, 1),
# )

removed_knights = 0

while True:
    max_attacks = 0
    knight_coord = []

    for row_i in range(board_size):
        for col_i in range(board_size):
            if matrix[row_i][col_i] == 'K':
                attacks = 0

                for move in moves:
                    move_row = row_i + move[0]
                    move_col = col_i + move[1]

                    if could_attack(move_row, move_col, board_size):
                        attacks += 1
                if attacks > max_attacks:
                    knight_coord = [row_i, col_i]
                    max_attacks = attacks
    if knight_coord:
        r, c = knight_coord
        matrix[r][c] = 0
        removed_knights += 1
    else:
        break

print(removed_knights)
