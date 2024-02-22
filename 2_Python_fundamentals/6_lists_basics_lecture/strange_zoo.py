first_position = input()
second_position = input()
third_position = input()
my_list = [first_position, second_position, third_position]
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)