row, col = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(row)]
result_counter = 0

for row_i in range(row-1):
    for col_i in range(col-1):

        a = matrix[row_i][col_i]
        b = matrix[row_i][col_i+1]
        c = matrix[row_i+1][col_i]
        d = matrix[row_i+1][col_i+1]

        if all(x == a for x in [b, c, d]):
            result_counter += 1

print(result_counter)
