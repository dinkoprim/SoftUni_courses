n = int(input())
evens_sum = 0
odds_sum = 0
for i in range(n):
    user_numbers = int(input())
    if i % 2 == 0:
        evens_sum += user_numbers
    else:
        odds_sum += user_numbers
if evens_sum == odds_sum:
    print(f'Yes')
    print(f'Sum = {evens_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(evens_sum - odds_sum)}')
