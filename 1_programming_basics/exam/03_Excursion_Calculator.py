group_members = int(input())
season = input()
ticket = 0
if group_members <= 5:
    if season == 'spring':
        ticket = 50
    elif season == 'summer':
        ticket = 48.50
    elif season == 'autumn':
        ticket = 60
    elif season == 'winter':
        ticket = 86
else:
    if season == 'spring':
        ticket = 48
    elif season == 'summer':
        ticket = 45
    elif season == 'autumn':
        ticket = 49.5
    elif season == 'winter':
        ticket = 85

cost = ticket * group_members

if season == 'winter':
    cost *= 1.08
elif season == 'summer':
    cost *= 0.85

print(f'{cost:.2f} leva.')
