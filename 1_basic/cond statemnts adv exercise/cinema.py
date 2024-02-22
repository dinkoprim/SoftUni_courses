event = input()
rows = int(input())
columns = int(input())
seats = rows * columns
ticket = 0
if event == 'Premiere':
    ticket = 12
elif event == 'Normal':
    ticket = 7.5
elif event == 'Discount':
    ticket = 5
hall_revenue = ticket * seats
print(f'{hall_revenue:.2f} leva')
