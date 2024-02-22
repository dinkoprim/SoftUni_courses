# flat = []
#
# flat = [flat.extend(el) for el in [[int(x) for x in input().split(', ')] for row_index in range(int(input()))]]
#
# print(flat)

print([item for row_index in range(int(input())) for item in [int(x) for x in input().split(', ')]])

