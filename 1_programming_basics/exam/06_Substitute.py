
K = int(input())
L = int(input())
M = int(input())
N = int(input())
counter = 0

for digit1 in range(K, 9):
    for digit2 in range(9, L - 1, -1):
        for digit3 in range(M, 9):
            for digit4 in range(9, N - 1, -1):
                if (digit1 % 2 == 0 and digit3 % 2 == 0) and (digit2 % 2 == 1 and digit4 % 2 == 1):
                    if str(digit1) + str(digit2) != str(digit3) + str(digit4):
                        print(f'{digit1}{digit2} - {digit3}{digit4}')
                        counter += 1
                    else:
                        print(f"Cannot change the same player.")
                    if counter == 6:
                        exit()
