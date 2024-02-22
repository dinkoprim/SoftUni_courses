n = float(input())
result = 0

if n == 0:
    result = "zero"
elif n > 0:
    result = "positive"
elif n < 0:
    result = "negative"

if 0 < abs(n) < 1:
    result = f'small {result}'
elif abs(n) > 1000000:
    result = f'large {result}'

print(result)


