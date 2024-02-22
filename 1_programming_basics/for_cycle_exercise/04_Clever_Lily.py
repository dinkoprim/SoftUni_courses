age = int(input())
machine_cost = float(input())
toy_price = int(input())
money = 0
toy_count = 0
money_present = 10

for running_year in range(1, age + 1):
    if running_year % 2 == 0:
        money += money_present - 1
        money_present += 10
    else:
        toy_count += 1

toy_debit = toy_count * toy_price
budget = toy_debit + money
diff = abs(budget - machine_cost)

if machine_cost <= budget:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
