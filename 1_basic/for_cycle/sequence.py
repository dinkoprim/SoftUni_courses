n = int(input())
max_num = 0
min_num = 0

for i in range(0, n):
    user_input = int(input())
    if i == 0:
        min_num = max_num = user_input
    else:
        if user_input > max_num:
            max_num = user_input
        if user_input < min_num:
            min_num = user_input

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
