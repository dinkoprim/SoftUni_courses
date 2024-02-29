heroes_count = int(input())
heroes_roster = [input().split(' ') for i in range(heroes_count)]


def heroes(roster):
    while True:
        command = input()
        if command == 'End':
            break

        command = command.split(' - ')
        action = command[0]
        hero_name = command[1]

        for hero_stats in roster:
            hero_hp = int(hero_stats[1])
            hero_mp = int(hero_stats[2])
            if action == "CastSpell":
                mp_needed = int(command[2])
                spell_name = command[3]
                if hero_name == hero_stats[0]:
                    if hero_mp >= mp_needed:
                        mana_left = hero_mp - mp_needed
                        print(f"{hero_name} has successfully cast {spell_name} and now has {mana_left} MP!")
                        hero_stats[2] = mana_left
                    else:
                        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
            elif action == "TakeDamage":
                damage = int(command[2])
                attacker = command[3]
                if hero_name == hero_stats[0]:
                    current_hp = hero_hp - damage
                    if current_hp > 0:
                        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
                        hero_stats[1] = current_hp
                    else:
                        print(f"{hero_name} has been killed by {attacker}!")
                        heroes_roster.remove(hero_stats)
            elif action == "Recharge":
                if hero_name == hero_stats[0]:
                    amount_recovered = int(command[2])
                    current_mp = hero_mp + amount_recovered
                    if current_mp >= 200:
                        current_mp = 200
                        amount_recovered = 200 - hero_mp
                    print(f"{hero_name} recharged for {amount_recovered} MP!")
                    hero_stats[2] = current_mp
            elif action == "Heal":
                if hero_name == hero_stats[0]:
                    amount_recovered = int(command[2])
                    current_hp = hero_hp + amount_recovered
                    if current_hp >= 100:
                        current_hp = 100
                        amount_recovered = 100 - hero_hp
                    print(f"{hero_name} healed for {amount_recovered} HP!")
                    hero_stats[1] = current_hp

    for hero_stats in roster:
        hero_name, hero_hp, hero_mp = hero_stats
        print(f"{hero_name}\n  HP: {hero_hp}\n  MP: {hero_mp}")


result = heroes(heroes_roster)
