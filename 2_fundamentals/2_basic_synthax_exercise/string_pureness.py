number_of_strings = int(input())
for i in range(number_of_strings):
    string = str(input())
    is_pure = True
    for j in string:
        if j in (".", ",", "_"):
            print(f'{string} is not pure!')
            is_pure = False
            break
    if is_pure:
        print(f'{string} is pure.')

