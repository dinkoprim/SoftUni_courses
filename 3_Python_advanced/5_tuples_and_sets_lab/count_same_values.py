numbers = tuple(float(el) for el in input().split())

checked_nums = {}

for num in numbers:
	if num not in checked_nums:
		checked_nums[num] = numbers.count(num)

for number, occur in checked_nums.items():
	print(f"{number} - {occur} times")
