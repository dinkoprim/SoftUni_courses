def index_of_evens(num_string):
    num_list = list(map(int, num_string.split(', ')))
    result = [num_list.index(num) for num in num_list if num % 2 == 0]
    return result


user_string = input()
print(index_of_evens(user_string))
