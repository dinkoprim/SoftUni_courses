sequences = {'First': set(int(x) for x in input().split()), 'Second': set(int(x) for x in input().split())}

for _ in range(int(input())):
	action, target, *data = input().split()

	if action == 'Add':
		sequences[target].update(map(int, data))

	elif action == 'Remove':
		sequences[target].difference_update(map(int, data))

	elif action == 'Check':
		print(sequences['First'].issubset(sequences['Second']) or sequences['Second'].issubset(sequences['First']))

print(*sorted(sequences['First']), sep=', ')
print(*sorted(sequences['Second']), sep=', ')
