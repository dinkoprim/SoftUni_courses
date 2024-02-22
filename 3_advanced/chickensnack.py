from collections import deque

money = [int(x) for x in input().split()]
prices = deque([int(x) for x in input().split()])

food_count = 0

while money and prices:
    curr_money = money.pop()
    curr_price = prices.popleft()

    if curr_money == curr_price:
        food_count += 1

    elif curr_money > curr_price:
        change = curr_money - curr_price
        if money:
            money[-1] += change
        else:
            money.append(change)
        food_count += 1

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif 1 < food_count < 4:
    print(f"Henry ate: {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
