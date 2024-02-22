from collections import deque
water_amount = int(input())
name = input()
dispenser_que = deque([])

while name != 'Start':
	dispenser_que.append(name)
	name = input()

command = input()

while command != 'End':
	tokens = command.split()

	if len(tokens) == 1:
		requested_amount = int(tokens[0])
		if requested_amount <= water_amount:
			print(f"{dispenser_que.popleft()} got water")
			water_amount -= requested_amount
		else:
			print(f"{dispenser_que.popleft()} must wait")
	else:
		water_amount += int(tokens[1])

	command = input()

print(f"{water_amount} liters left")
