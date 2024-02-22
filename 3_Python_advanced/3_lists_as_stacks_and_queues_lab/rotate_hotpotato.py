from collections import deque
names = deque(input().split())
n_tosses = int(input()) - 1

while len(names) > 1:
	names.rotate(-n_tosses)
	print(f'Removed {names.popleft()}')

print(f'Last is {names.pop()}')
