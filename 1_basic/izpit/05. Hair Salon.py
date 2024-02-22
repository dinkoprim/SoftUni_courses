goal = int(input())
balance = 0
while True:
    user_input = input()
    if user_input == 'closed':
        break
    elif user_input == 'haircut':
        what_kind = input()
        if what_kind == 'mens':
            balance += 15
        elif what_kind == 'ladies':
            balance += 20
        elif what_kind == 'kids':
            balance += 10
    elif user_input == 'color':
        what_color = input()
        if what_color == 'touch up':
            balance += 20
        elif what_color == 'full color':
            balance += 30
    if balance >= goal:
        break


if balance < goal:
    print(f"Target not reached! You need {goal - balance}lv. more.")
    print(f"Earned money: {balance}lv.")
else:
    print(f"You have reached your target for the day!")
    print(f"Earned money: {balance}lv.")

