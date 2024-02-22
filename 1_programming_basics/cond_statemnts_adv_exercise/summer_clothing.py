temp = int(input())
daytime = str(input())
outfit = 0
shoes = 0
if 10 <= temp <= 18:
    if daytime == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif daytime == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif daytime == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < temp <= 24:
    if daytime == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif daytime == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif daytime == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif temp >= 25:
    if daytime == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif daytime == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif daytime == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {temp} degrees, get your {outfit} and {shoes}.")
