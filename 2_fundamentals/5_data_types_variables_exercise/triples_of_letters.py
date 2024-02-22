index = int(input())
for i in range(index):
    for j in range(index):
        for k in range(index):
            print(f'{chr(97+i)}{chr(97+j)}{chr(97+k)}')