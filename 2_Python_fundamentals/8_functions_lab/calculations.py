def solve(operator, a, b):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


input_operator = input()
first_num = int(input())
second_num = int(input())
print(f'{solve(input_operator, first_num, second_num):.0f}')
