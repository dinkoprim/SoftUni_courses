rows, cols = [int(x) for x in input().split()]
matrix = [['']*cols for _ in range(rows)]
row_ascii = ord('a')

for row_i in range(rows):
    for col_i in range(cols):

        element = chr(row_ascii) + chr(row_ascii + col_i) + chr(row_ascii)

        matrix[row_i][col_i] = element

    row_ascii += 1

for row in matrix:
    print(*row)

