budget = int(input())
season = str(input())
count_fisherman = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600
if count_fisherman <= 6:
    price *= 0.9
elif 7 <= count_fisherman <= 11:
    price *= 0.85
elif count_fisherman > 12:
    price *= 0.75

if season == 'Summer' or season == 'Spring' or season == 'Winter':
    if count_fisherman % 2 == 0:
        price *= 0.95

diff = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
