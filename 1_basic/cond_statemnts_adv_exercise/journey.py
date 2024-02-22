budget = float(input())
season = input()
booking = 'Hotel'
destination = ''
expense = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        booking = 'Camp'
        expense = budget * 0.3
    elif season == 'winter':
        booking = 'Hotel'
        expense = budget * 0.7
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        booking = 'Camp'
        expense = budget * 0.4
    elif season == 'winter':
        booking = 'Hotel'
        expense = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    expense = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{booking} - {expense:.2f}")

