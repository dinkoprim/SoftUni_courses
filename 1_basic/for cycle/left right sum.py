n = int(input())
left_sum = 0
right_sum = 0
for i in range(n):
    user_number = int(input())
    left_sum += user_number
for i in range(n):
    user_number = int(input())
    right_sum += user_number
if left_sum == right_sum:
    result = f"Yes, sum = {left_sum}"
else:
    diff = abs(left_sum - right_sum)
    result = f"No, diff = {diff}"
print(result)
