# matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
#
# left_diagonal = []
# right_diagonal = []
#
# for row_i in range(len(matrix)):
#     left_num = matrix[row_i][row_i]
#     right_num = matrix[row_i][(len(matrix)-1) - row_i]
#     left_diagonal.append(left_num), right_diagonal.append(right_num)
#
# print(f'Primary diagonal: {', '.join(map(str, left_diagonal))}. Sum:{sum(left_diagonal)}')
# print(f'Secondary diagonal: {', '.join(map(str, right_diagonal))}. Sum:{sum(right_diagonal)}')


matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]

primary = [matrix[r][r] for r in range(len(matrix))]

secondary = [matrix[r][(len(matrix)-1) - r] for r in range(len(matrix))]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
