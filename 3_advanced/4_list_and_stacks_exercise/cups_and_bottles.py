from collections import deque
cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())
wasted_liters = 0
while cups and bottles:
	current_cup = cups.popleft()
	current_bottle = bottles.pop()
	if current_cup <= current_bottle:
		wasted_liters += current_bottle - current_cup

	else:
		current_cup = current_cup - current_bottle
		cups.appendleft(current_cup)

if not cups:
	print(f"Bottles:", *bottles)
if not bottles:
	print(f"Cups:", *cups)
print(f"Wasted litters of water: {wasted_liters}")