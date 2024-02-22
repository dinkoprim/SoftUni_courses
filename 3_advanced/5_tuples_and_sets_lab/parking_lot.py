n = int(input())
cars = set()
for _ in range(n):
	direction, car_No = input().split(', ')

	if direction == "IN":
		cars.add(car_No)
	elif direction == "OUT":
		if car_No in cars:
			cars.remove(car_No)

if not cars:
	print(f'Parking Lot is Empty')
else:
	print(*cars, sep='\n')
