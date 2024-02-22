# from collections import deque
# from math import floor
#
# expression = deque(input().split())
#
# idx = 0
#
# while idx < len(expression):
# 	el = expression[idx]
#
# 	if el == "*":
# 		for _ in range(idx - 1):
# 			expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
# 	elif el== "/":
# 		for _ in range(idx - 1):
# 			expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
# 	elif el == "-":
# 		for _ in range(idx - 1):
# 			expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
# 	elif el == "+":
# 		for _ in range(idx - 1):
# 			expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
#
# 	if el in "/*+-":
# 		del expression[1]
# 		idx = 1
#
# 	idx += 1
#
# print(floor(int(expression[0])))

from collections import deque
from math import floor


def evaluate_expression(expression):
    numbers = deque()
    operators = ["*", "+", "-", "/"]
    expression_list = expression.split()

    for el in expression_list:
        if el not in operators:
            numbers.append(int(el))
        else:
            if el == "+":
                while len(numbers) >= 2:
                    numbers.appendleft(numbers.popleft() + numbers.popleft())
            elif el == "-":
                while len(numbers) >= 2:
                    numbers.appendleft(numbers.popleft() - numbers.popleft())
            elif el == "*":
                while len(numbers) >= 2:
                    numbers.appendleft(numbers.popleft() * numbers.popleft())
            elif el == "/":
                while len(numbers) >= 2:
                    num1, num2 = numbers.popleft(), numbers.popleft()
                    numbers.appendleft(floor(num1 / num2))

    return numbers[0]


expression_input = input()
result = evaluate_expression(expression_input)
print(result)

