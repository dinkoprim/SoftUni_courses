lost_games = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_counter = 0
for game_number in range(1, lost_games + 1):
    if game_number % 2 == 0:
        expenses += helmet_price
    if game_number % 3 == 0:
        expenses += sword_price
        if game_number % 2 == 0:
            expenses += shield_price
            shield_counter += 1
            if shield_counter % 2 == 0:
                expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
