all_intersections = []

for _ in range(int(input())):

	data_1, data_2 = input().split('-')
	first_start, first_end = map(int, data_1.split(','))
	second_start, second_end = map(int, data_2.split(','))

	first_set = set(range(first_start, first_end + 1))
	second_set = set(range(second_start, second_end + 1))

	intersection = first_set.intersection(second_set)
	all_intersections.append(intersection)

longest = max(all_intersections, key=len)

print(f"Longest intersection is {list(longest)} with length {len(longest)}")