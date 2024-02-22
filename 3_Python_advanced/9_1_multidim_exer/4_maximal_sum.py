rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
maximal_sum = float('-inf')
biggest_matrix = []

for row_i in range(rows - 2):
    for col_i in range(cols - 2):

        grid_row_1 = matrix[row_i][col_i:col_i+3]
        grid_row_2 = matrix[row_i+1][col_i:col_i+3]
        grid_row_3 = matrix[row_i+2][col_i:col_i+3]

        grid_sum = sum(grid_row_1) + sum(grid_row_2) + sum(grid_row_3)

        if grid_sum > maximal_sum:
            maximal_sum = grid_sum
            biggest_matrix = [grid_row_1, grid_row_2, grid_row_3]

print(f'Sum = {maximal_sum}')
for row in biggest_matrix:
    print(*row)
