from collections import deque

chocolates = [int(x) for x in input().split(',')]
milk = deque(int(x) for x in input().split(','))

milkshakes = 0

while chocolates and milk and milkshakes != 5:

    curr_choc = chocolates.pop()
    curr_milk = milk.popleft()

    if curr_choc <= 0 and curr_milk <= 0:
        continue
    elif curr_choc <= 0:
        milk.appendleft(curr_milk)
        continue
    elif curr_milk <= 0:
        chocolates.append(curr_choc)
        continue

    milkshakes += 1 if curr_choc == curr_milk else 0

    if curr_choc != curr_milk:
        milk.append(curr_milk)
        chocolates.append(curr_choc - 5)


print(f"Great! You made all the chocolate milkshakes needed!" if milkshakes > 4 else "Not enough milkshakes.")
print(f'Chocolate: ' + ', '.join(map(str, chocolates)) if chocolates else f'Chocolate: empty')
print(f'Milk: ' + ', '.join(map(str, milk)) if milk else f'Milk: empty')
