# row_count = int(input())

# print([list([int(x) for x in input().split(', ') if int(x) % 2 == 0]) for row_idx in range(int(input()))])

# evens_matrix = [(list([el for el in row_idx if el % 2 == 0])) for row_idx in matrix]

# print(evens_matrix)

print(list([[int(x) for x in input().split(', ') if int(x) % 2 == 0] for row in range(int(input()))]))
