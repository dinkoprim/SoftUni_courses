month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
cost_studio = 0
cost_apartment = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 < nights <= 14:
        cost_studio = studio_price * nights * 0.95
    elif 14 < nights:
        cost_studio = studio_price * nights * 0.7
    else:
        cost_studio = studio_price * nights
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if 14 < nights:
        cost_studio = studio_price * nights * 0.8
    else:
        cost_studio = studio_price * nights
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
    cost_studio = studio_price * nights
if nights > 14:
    cost_apartment = apartment_price * nights * 0.9
else:
    cost_apartment = apartment_price * nights

print(f'Apartment: {cost_apartment:.2f} lv.')
print(f'Studio: {cost_studio:.2f} lv.')
