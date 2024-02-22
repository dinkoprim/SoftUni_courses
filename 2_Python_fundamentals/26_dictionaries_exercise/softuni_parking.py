parking = {}
n = int(input())

for _ in range(n):
    cmd, *driver_info = input().split()
    username = driver_info[0]

    if cmd == 'register':

        plate = driver_info[1]

        if username not in parking.keys():
            parking[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")

    elif cmd == 'unregister':

        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

[print(f'{k} => {v}') for k, v in parking.items()]
