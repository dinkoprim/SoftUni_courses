def is_even(n):

    if int(n) % 2 == 0:
        return True
    return False


sequence = input().split(' ')
even_numbers = list(filter(is_even, sequence))
numbers_list = list(map(int, even_numbers))
print(numbers_list)