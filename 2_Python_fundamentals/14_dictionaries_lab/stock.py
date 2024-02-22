line = input().split()
stock = {}

for i in range(0, len(line), 2):
	product = line[i]
	quantity = line[i + 1]
	stock[product] = quantity

check_products = input().split()

for item in check_products:
	if item in stock.keys():
		quantity = stock[item]
		print(f"We have {quantity} of {item} left")
	else:
		print(f"Sorry, we don't have {item}")
