number_of_orders = int(input())
total = 0
for i in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_capsule < 0.01 or price_capsule > 100:
        continue
    if days > 31 or days < 1:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    order_price = (price_capsule * capsules_per_day) * days
    print(f"The price for the coffee is: ${order_price:.2f}")
    total += order_price

print(f"Total: ${total:.2f}")