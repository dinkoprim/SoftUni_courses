collection_of_items = input().split('|')
budget_left = float(input())
items_with_markup = []
expenses = 0
for element in collection_of_items:
    items_details = element.split('->')
    item_type = items_details[0]
    item_price = float(items_details[1])
    if item_type == 'Clothes':
        if item_price > 50:
            continue
    elif item_type == 'Shoes':
        if item_price > 35:
            continue
    elif item_type == 'Accessories':
        if item_price > 20.50:
            continue
    if item_price <= budget_left:
        expenses += item_price
        budget_left -= item_price
        new_price = item_price * 1.4
        items_with_markup.append(new_price)

profit = expenses * 0.4
new_budget = profit + budget_left + expenses

for element in range(len(items_with_markup)):
    print(f'{items_with_markup[element]:.2f}', end=' ')
print()
print(f"Profit: {profit:.2f}")

if new_budget >= 150:
    print(f'Hello, France!')
else:
    print(f"Not enough money.")