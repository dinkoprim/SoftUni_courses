import sys

n = int(input())
sum_numbers = 0
max_number = -sys.maxsize

for index in range(n):
    number = int(input())

    if number > max_number:
        max_number = number
    sum_numbers += number

sum_numbers -= max_number

if max_number == sum_numbers:
    print(f'Yes')
    print(f'Sum = {sum_numbers}')
else:
    print(f'No')
    print(f'Diff = {abs(sum_numbers-max_number)}')
