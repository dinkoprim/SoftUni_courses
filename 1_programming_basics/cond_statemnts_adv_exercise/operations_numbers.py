n1 = int(input())
n2 = int(input())
operator = input()
result = 0
type_number = ""

if operator == '+' or operator== '-' or operator== '*':
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2

    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {type_number}')

if operator == '/' and n2 != 0:
    result = n1 / n2
    print(f'{n1} {operator} {n2} = {result:.2f}')
elif operator == '%' and n2 != 0:
    result = n1 % n2
    print(f'{n1} {operator} {n2} = {result}')

if n2 == 0:
    print(f"Cannot divide {n1} by zero")






