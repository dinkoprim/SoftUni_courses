row, col = list(map(int, input().split(', ')))
matrix = [[int(x) for x in input().split(', ')] for row_i in range(row)]
biggest_sum = float('-inf')
biggest_matrix = []

for row_i in range(row-1):
    for col_i in range(col-1):

            a = matrix[row_i][col_i]
            b = matrix[row_i][col_i+1]
            c = matrix[row_i+1][col_i]
            d = matrix[row_i+1][col_i+1]

            sector_matrix = [
                [a, b],
                [c, d],
            ]
            sector_sum = a + b + c + d

            if sector_sum > biggest_sum:
                biggest_sum = sector_sum
                biggest_matrix = sector_matrix

for row in biggest_matrix:
    print(*row)
print(biggest_sum)
