from collections import deque
my_stack = deque()

for _ in range(int(input())):
	line = [int(x) for x in input().split()]  # simultaneously transforms the command into int and
												# splits it for tokens only with one line comprehension !!!
	command = line[0]

	if command == 1:
		my_stack.append(line[1])

	if my_stack:
		if command == 2:
			my_stack.pop()

		elif command == 3:
			print(max(my_stack))
		elif command == 4:
			print(min(my_stack))

my_stack.reverse()
print(', '.join(map(str, my_stack)))
