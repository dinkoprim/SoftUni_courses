def sum_numbers(a, b):
    return a + b


def subtract(sum, c):
    return sum - c


def add_and_subtract(a, b, c):
    a_plus_b = sum_numbers(a, b)
    c_minus_sum = subtract(a_plus_b, c)
    return c_minus_sum

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))