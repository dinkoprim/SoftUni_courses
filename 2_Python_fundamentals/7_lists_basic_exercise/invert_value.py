numbers_string = input().split()
opposites_list = []
for numbers in numbers_string:
    numbers = int(numbers)
    opposite_number = numbers * -1
    opposites_list.append(opposite_number)
print(opposites_list)