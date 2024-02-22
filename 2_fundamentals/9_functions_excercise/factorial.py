first_number = int(input())
second_number = int(input())
def factorial_division(a, b):
    factorial_a = a
    factorial_b = b
    for n in range(1, a):
        factorial_a *= a - n
    for n in range(1, b):
        factorial_b *= b - n
    result = factorial_a / factorial_b
    return f"{result:.2f}"


print(factorial_division(first_number, second_number))