user_line = input().split('|')
matrix = [[int(x) for x in el.split()] for el in user_line]

print(*[element for row in matrix[::-1] for element in row])
