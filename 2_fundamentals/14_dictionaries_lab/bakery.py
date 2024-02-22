bakery_items = input().split()
bakery_dict = {}
for i in range(0, len(bakery_items), 2):
	item = bakery_items[i]
	stock = int(bakery_items[i + 1])
	bakery_dict[item] = stock

print(bakery_dict)