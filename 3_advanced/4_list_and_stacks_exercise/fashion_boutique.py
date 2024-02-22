from collections import deque

items = deque([int(x) for x in input().split()])
rack_space = int(input())
current_rack_space = rack_space
racks_count = 1

while items:
	current_item = items.pop()

	if current_rack_space >= current_item:
		current_rack_space -= current_item

	else:
		racks_count += 1
		current_rack_space = rack_space - current_item


print(racks_count)
