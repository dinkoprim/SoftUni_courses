days_of_stay = int(input())
room_type = input()
feedback = input()
single_room = (days_of_stay - 1) * 18
apartment = (days_of_stay - 1) * 25
president_apartment = (days_of_stay - 1) * 35
if 0 < days_of_stay < 10:
    apartment *= 0.7
    president_apartment *= 0.9
elif 10 < days_of_stay < 15:
    apartment *= 0.65
    president_apartment *= 0.85
elif days_of_stay > 15:
    apartment *= 0.5
    president_apartment *= 0.8
if feedback == 'positive':
    single_room *= 1.25
    apartment *= 1.25
    president_apartment *= 1.25
elif feedback == 'negative':
    single_room *= 0.9
    apartment *= 0.9
    president_apartment *= 0.9
if room_type == 'room for one person':
    print(f'{single_room:.2f}')
elif room_type == 'apartment':
    print(f'{apartment:.2f}')
elif room_type == 'president apartment':
    print(f'{president_apartment:.2f}')
