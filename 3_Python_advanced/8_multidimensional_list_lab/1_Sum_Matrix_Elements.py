row, col = [int(x) for x in input().split(', ')]
matrix = []
total = 0

for row in range(row):
    row_data = [int(x) for x in input().split(', ')]
    total += sum(row_data)
    matrix.append(row_data)

print(total)
print(matrix)