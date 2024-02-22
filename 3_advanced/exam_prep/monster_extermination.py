from collections import deque

monsters_armor = deque(int(x) for x in input().split(','))
impact_strength = [int(x) for x in input().split(',')]
killed_monsters = 0

while monsters_armor and impact_strength:
    monster = monsters_armor.popleft()
    strike = impact_strength.pop()

    if strike >= monster:
        remaining_power = strike - monster
        killed_monsters += 1
        if remaining_power > 0:
            if not impact_strength:
                impact_strength.append(remaining_power)
            else:
                impact_strength[-1] += remaining_power
    elif strike < monster:
        wounded_monster = monster - strike
        monsters_armor.append(wounded_monster)

if not monsters_armor:
    print("All monsters have been killed!")
if not impact_strength:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")