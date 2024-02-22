def odd_even_separator(given_number):
    even_sum = 0
    odd_sum = 0
    numbers_list = list(map(int, given_number))
    for digit in numbers_list:
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return even_sum, odd_sum


user_number = input()
even_sum, odd_sum = odd_even_separator(user_number)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
