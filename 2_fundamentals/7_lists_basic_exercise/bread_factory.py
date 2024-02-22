total_energy = 100
total_coins = 100
working_day_events = input().split('|')
factory_opened = True
for event in working_day_events:
    event_details = event.split('-')
    type_of_event = event_details[0]
    value_of_event = int(event_details[1])
    if type_of_event == 'rest':
        energy_pool = total_energy
        total_energy += value_of_event
        if total_energy > 100:
            total_energy = 100
        print(f"You gained {total_energy - energy_pool} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == 'order':
        if total_energy >= 30:
            total_coins += value_of_event
            total_energy -= 30
            print(f"You earned {value_of_event} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if total_coins >= value_of_event:
            total_coins -= value_of_event
            print(f"You bought {type_of_event}.")
        else:
            factory_opened = False
            print(f"Closed! Cannot afford {type_of_event}.")
            break

if factory_opened:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
