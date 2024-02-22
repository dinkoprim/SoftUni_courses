flower_type = str(input())
count_flowers = int(input())
budget = int(input())
bill = 0

if flower_type == 'Roses':
    bill = 5 * count_flowers
    if count_flowers > 80:
        bill *= 0.9
elif flower_type == 'Dahlias':
    bill = 3.80 * count_flowers
    if count_flowers > 90:
        bill *= 0.85
elif flower_type == 'Tulips':
    bill = 2.80 * count_flowers
    if count_flowers > 80:
        bill *= 0.85
elif flower_type == 'Narcissus':
    bill = 3 * count_flowers
    if count_flowers < 120:
        bill *= 1.15
elif flower_type == 'Gladiolus':
    bill = 2.5 * count_flowers
    if count_flowers < 80:
        bill *= 1.2
money_diff = abs(budget - bill)
if budget >= bill:
    print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {money_diff:.2f} leva left.")
else:
    print(f'Not enough money, you need {money_diff:.2f} leva more.')
