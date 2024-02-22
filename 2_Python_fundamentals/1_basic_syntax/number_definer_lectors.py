n = float(input())
result = 0
if n == 0:
    result = "zero"
elif n > 0:
    if n < 1:
        result = "small positive"
    elif n > 1000000:
        result = "large positive"
    else:
        result = "positive"
else:
    if abs(n) < 1:
        result = "small negative"
    elif abs(n) > 1000000:
        result = "large negative"
    else:
        result = "negative"

print(result)