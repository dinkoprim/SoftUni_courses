fruit = input()
day = input()
qty = float(input())
price = 'error'
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' \
    or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = qty * 2.5
    elif fruit == 'apple':
        price = qty * 1.2
    elif fruit == 'orange':
        price = qty * 0.85
    elif fruit == 'grapefruit':
        price = qty * 1.45
    elif fruit == 'kiwi':
        price = qty * 2.70
    elif fruit == 'pineapple':
        price = qty * 5.50
    elif fruit == 'grapes':
        price = qty * 3.85
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = qty * 2.7
    elif fruit == 'apple':
        price = qty * 1.25
    elif fruit == 'orange':
        price = qty * 0.90
    elif fruit == 'grapefruit':
        price = qty * 1.60
    elif fruit == 'kiwi':
        price = qty * 3
    elif fruit == 'pineapple':
        price = qty * 5.60
    elif fruit == 'grapes':
        price = qty * 4.2
if price == 'error':
    print(price)
else:
    print(f'{price:.2f}')
