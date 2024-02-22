income = float(input()) * 5
profit = float(input()) * 5
total_saved = income + profit
expenses = float(input())
balance = total_saved - expenses
goal = float(input())
if balance > goal:
    print(f"Profit: {balance:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {goal - balance:.2f} BGN.")
