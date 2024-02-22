# def board_print():
#     for row in board:
#         print(row)
#
# def board_full(field):
#
#     if field[0].count(0):
#         board_print()
#
#
#
# board = [[0] * 3 for rows in range(3)]
# board[0] = [1, 2, 3]
# board_full(board)

# matrix = [[0]*3]*3
# for row in matrix:
#     print(row)

#
# a = [1, 2, 3, 4, 5]
# print(a[:])
# print(str(a)[1:-1])

# lst = [1]
# lst[-1] += 1
# print(lst)
#
# text = f""" mnogoredov string
# asda
# da
# daa
# {lst} asdasda
# """
#
# print(text)

# text = 'hello'
#
# print(text.find('h'))

line = input()
name, (price, qty) = line.split()
print(name)
print(price)
print(qty)