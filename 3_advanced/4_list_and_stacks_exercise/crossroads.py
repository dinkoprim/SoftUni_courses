from collections import deque
line_of_cars = deque()
green_duration = int(input())
free_window = int(input())

while True:
	command = input()
	if command == 'END':
		break

	if command == 'green':
		current_car = line_of_cars.popleft()
		if len(current_car) > green_duration:
			continue

	line_of_cars.append(command)
