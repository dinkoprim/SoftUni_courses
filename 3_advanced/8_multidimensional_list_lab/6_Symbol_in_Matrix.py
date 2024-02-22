matrix = [list(input()) for _ in range(int(input()))]
symbol = input()
result = ()

for row_i in range(len(matrix)):
    for col_i in range(len(matrix[row_i])):
        if matrix[row_i][col_i] == symbol:
            result = (row_i, col_i)
            print(result)
            exit()

print(f"{symbol} does not occur in the matrix")
