def supply_calc():
    starting_food = float(input())
    starting_hay = float(input())
    starting_cover = float(input())
    pigs_weight = float(input())
    excess_food, excess_hay, excess_cover = (
        starting_food, starting_hay, starting_cover)
    for day in range(1, 31):

        excess_food = round((excess_food - 0.3), 3)
        if day % 2 == 0:
            hay_used = round(0.05 * excess_food, 3)
            excess_hay = round((excess_hay - hay_used), 3)
        if day % 3 == 0:
            cover_used = pigs_weight / 3
            excess_cover = round((excess_cover - cover_used), 3)
        if excess_food <= 0 or excess_cover <= 0 or excess_hay <= 0:
            print(f"Merry must go to the pet store!")
            break

    else:
        print(f"Everything is fine! Puppy is happy! Food: "
              f"{excess_food:.2f}, Hay: {excess_hay:.2f}, Cover: {excess_cover:.2f}.")


run = supply_calc()
