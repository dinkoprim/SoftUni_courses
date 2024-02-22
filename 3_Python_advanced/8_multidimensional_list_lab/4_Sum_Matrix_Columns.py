row, col = map(int, input().split(', '))

matrix = []
column_sum = 0

for _ in range(row):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for col_index in range(col):
    for row_index in range(row):
        column_sum += matrix[row_index][col_index]
    print(column_sum)
    column_sum = 0
