from collections import deque

food = int(input())
orders = deque(map(int, input().split()))
print(max(orders))
while orders:
	if food >= orders[0]:
		food -= orders.popleft()
	else:
		break

if not orders:
	print(f"Orders complete")
else:
	print(f"Orders left:", *orders)
	