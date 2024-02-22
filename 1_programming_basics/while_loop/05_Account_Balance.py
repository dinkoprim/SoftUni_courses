balance = 0
while True:
    debit = input()
    if debit == "NoMoreMoney":
        break
    debit = float(debit)
    if debit < 0:
        print(f"Invalid operation!")
        break
    balance += debit
    print(f'Increase: {debit:.2f}')
print(f'Total: {balance:.2f}')