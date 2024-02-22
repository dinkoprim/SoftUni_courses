decoration_quantity = int(input())
days_till_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
total_spirit = 0
for today in range(1, days_till_christmas + 1):

    if today % 11 == 0:
        decoration_quantity += 2

    if today % 2 == 0:
        total_cost += ornament_set_price * decoration_quantity
        total_spirit += 5

    if today % 3 == 0:
        total_cost += tree_skirt_price * decoration_quantity
        total_spirit += 3
        total_cost += tree_garland_price * decoration_quantity
        total_spirit += 10

    if today % 5 == 0:
        total_cost += tree_lights_price * decoration_quantity
        total_spirit += 17

        if today % 3 == 0:
            total_spirit += 30

    if today % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days_till_christmas % 10 == 0:
        total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

