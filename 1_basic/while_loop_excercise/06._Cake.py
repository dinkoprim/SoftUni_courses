a = int(input())
b = int(input())
pieces = input()
pieces_counter = 0
cake_size = a * b

while pieces != 'STOP':
    pieces = int(pieces)
    pieces_counter += pieces
    if pieces_counter >= cake_size:
        break

    pieces = input()


if pieces == 'STOP':
    print(f"{cake_size - pieces_counter} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_counter - cake_size} pieces more.")
