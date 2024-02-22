even_names = set()
odd_names = set()

for i in range(1, int(input()) + 1):

	name = int(sum(ord(char) for char in input())) // i

	if name % 2 == 0:
		even_names.add(name)
	else:
		odd_names.add(name)

even_sum, odd_sum = sum(even_names), sum(odd_names)

if even_sum == odd_sum:
	print(', '.join(map(str, even_names.union(odd_names))))

elif odd_sum > even_sum:
	print(', '.join(map(str, odd_names.difference(even_names))))

elif even_sum > odd_sum:
	print(', '.join(map(str, even_names.symmetric_difference(odd_names))))
