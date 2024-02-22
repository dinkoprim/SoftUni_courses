matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

primary = [matrix[r][r] for r in range(len(matrix))]

secondary = [matrix[r][(len(matrix)-1) - r] for r in range(len(matrix))]

print(abs(sum(primary) - sum(secondary)))
