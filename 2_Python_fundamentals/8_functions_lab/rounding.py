given_nums = input().split(' ')
rounded_numbers = []
for element in given_nums:
    num = float(element)
    rounded_numbers.append(round(num))
print(rounded_numbers)
