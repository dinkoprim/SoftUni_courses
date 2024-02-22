goal = float(input())
balance = float(input())
day_counter = 0
spent_counter = 0

while True:
    operation = input()
    amount = float(input())
    day_counter += 1

    if operation == 'spend':
        balance -= amount
        spent_counter += 1
        if balance <= 0:
            balance = 0
        if spent_counter >= 5:
            print(f"You can't save the money.")
            print(f"{day_counter}")
            break
    if operation == 'save':
        balance += amount
        spent_counter = 0
    if balance >= goal:
        print(f"You saved the money for {day_counter} days.")
        break
