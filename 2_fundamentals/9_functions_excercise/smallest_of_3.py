first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers_list = [first_number, second_number, third_number]


def smallest_finder(given_list):
    return min(given_list)


smallest_number = smallest_finder(numbers_list)
print(smallest_number)
