# input
product = str(input())
city = str(input())
quantity = float(input())
price = 0
# logic
if city == 'Sofia':
    if product == 'coffee':
        price = 0.5
    elif product == 'water':
        price = 0.8
    elif product == 'beer':
        price = 1.2
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.60
elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.4
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.30
    elif product == 'peanuts':
        price = 1.50
elif city == 'Varna':
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.10
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55
bill = price * quantity
# output
print(bill)
