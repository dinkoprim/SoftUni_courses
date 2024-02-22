# current_version = input().split('.')
# first_digit = int(current_version[0])
# second_digit = int(current_version[1])
# third_digit = int(current_version[2])
# third_digit += 1
# if third_digit > 9:
#     third_digit = 0
#     second_digit += 1
#     if second_digit > 9:
#         second_digit = 0
#         first_digit += 1
#
# new_version = list(map(str, [first_digit, second_digit, third_digit]))
# print('.'.join(new_version))

current_version = [num for num in input().split('.')]
new_version = int(''.join(current_version)) + 1
result = '.'.join(str(new_version))
print(result)

