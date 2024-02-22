from collections import deque

initial_fuel = [int(x) for x in input().split()]
add_consumption = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])

reached_altitudes = []
n = 0
failed = False

while initial_fuel:
    result = initial_fuel[-1] - add_consumption[0]

    if fuel_needed[0] > result:
        print(f"John did not reach: Altitude {n + 1}")
        failed = True
        break
    else:
        initial_fuel.pop()
        add_consumption.popleft()
        fuel_needed.popleft()
        n += 1
        print(f"John has reached: Altitude {n}")
        reached_altitudes.append(f'Altitude {n}')

if failed:
    if n == 0:
        print(f"John failed to reach the top.\nJohn didn't reach any altitude.")
    else:
        print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached_altitudes)}")
else:
    print(f"John has reached all the altitudes and managed to reach the top!")
