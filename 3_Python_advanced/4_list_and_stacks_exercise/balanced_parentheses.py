from collections import deque

line = deque(input())

def are_parentheses_balanced(brackets):
    stack = []
    opening_parentheses = "{[("
    closing_parentheses = "}])"

    for char in brackets:
        if char in opening_parentheses:
            stack.append(char)

        elif char in closing_parentheses:

            if not stack or opening_parentheses[closing_parentheses.index(char)] != stack.pop():
                return False

    return not stack


result = are_parentheses_balanced(line)

if result:
    print("YES")
else:
    print("NO")
