neighbourhood = list(map(int, input().split('@')))


def valentines_day(houses):
    visited_house = 0

    while True:
        command = input()

        if command == 'Love!':
            last_position = visited_house
            break

        command_parts = command.split(' ')
        length = int(command_parts[1])
        visited_house += length

        if length >= len(neighbourhood):
            visited_house = 0

        if visited_house > len(neighbourhood)-1:
            visited_house = 0

        if neighbourhood[visited_house] == 0:
            print(f"Place {visited_house} already had Valentine's day.")
        else:
            neighbourhood[visited_house] -= 2
            if neighbourhood[visited_house] <= 0:
                print(f"Place {visited_house} has Valentine's day.")

    print(f"Cupid's last position was {last_position}.")
    if all(houses == 0 for houses in neighbourhood):
        print(f"Mission was successful.")
    else:
        failed_houses = len(neighbourhood) - neighbourhood.count(0)
        print(f"Cupid has failed {failed_houses} places.")


run = valentines_day(neighbourhood)
