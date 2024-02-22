number_of_entries = int(input())
liters_total = 0

for i in range(number_of_entries):

    liters_added = int(input())
    liters_total += liters_added
    if liters_total > 255:
        print('Insufficient capacity!')
        liters_total -= liters_added
        continue

print(liters_total)

