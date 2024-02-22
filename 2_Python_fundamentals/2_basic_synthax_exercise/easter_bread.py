budget = float(input())
eggs = 0
loaf_counter = 0
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = (1.25 * flour_price) / 4
loaf_cost = flour_price + eggs_price + milk_price
loafs_to_make = budget // loaf_cost
money_left = budget - (loafs_to_make * loaf_cost)
for i in range(int(loafs_to_make)):
    loaf_counter += 1
    eggs += 3
    if loaf_counter % 3 == 0:
        eggs -= loaf_counter -2
print(f'You made {round(loafs_to_make)} loaves of Easter bread! Now you have {eggs} eggs and {money_left:.2f}BGN left.')