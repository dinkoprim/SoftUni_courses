n = int(input())
reservation_list = set()

for _ in range(n):
	reservation = input()
	reservation_list.add(reservation)

while True:
	guest = input()
	if guest == 'END':
		break

	if guest in reservation_list:
		reservation_list.remove(guest)

print(len(reservation_list))

for guest in sorted(reservation_list):
	print(guest)