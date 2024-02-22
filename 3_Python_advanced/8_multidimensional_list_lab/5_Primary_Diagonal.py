matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
result = 0

for row_i in range(len(matrix)):
    result += matrix[row_i][row_i]

print(result)