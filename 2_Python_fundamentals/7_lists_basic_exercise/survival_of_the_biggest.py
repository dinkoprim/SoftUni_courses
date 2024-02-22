numbers_list = input().split(' ')
numbers_to_remove = int(input())
counter = 0
for number in range(len(numbers_list)):
    numbers_list[number] = int(numbers_list[number])
while counter < numbers_to_remove:
    smallest_num = min(numbers_list)
    for number in numbers_list:
        if number == smallest_num:
            numbers_list.remove(number)
            counter += 1

for element in range(len(numbers_list)):
    numbers_list[element] = str(numbers_list[element])

print(', '.join(numbers_list))
