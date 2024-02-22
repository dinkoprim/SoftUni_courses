stock = {}
while True:
	command = input()
	if command == 'statistics':
		product_count = len(stock)
		total_quantity = sum(stock.values())
		print(f"Products in stock:")

		for key, value in stock.items():
			print(f"- {key}: {value}")

		print(f"Total Products: {product_count}\nTotal Quantity: {total_quantity}")
		break

	product, quantity = command.split(': ')
	quantity = int(quantity)

	if product not in stock:
		stock[product] = quantity
	else:
		stock[product] += quantity

	product_count = len(stock)
	total_quantity = sum(stock.values())
