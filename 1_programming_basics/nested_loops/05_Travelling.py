while True:
    destination = input()
    if destination == 'End':
        break
    cost = float(input())
    balance = 0
    while balance < cost:
        balance += float(input())
    print(f"Going to {destination}!")
