def is_perfect_number(some_number):
    divisor_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisor_sum += divisor
    if divisor_sum == some_number:
        return f'We have a perfect number!'

    return f"It's not so perfect."


user_number = int(input())
print(is_perfect_number(user_number))