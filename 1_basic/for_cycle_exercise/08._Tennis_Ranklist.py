from math import floor
tournaments_count = int(input())
points = int(input())
wins = 0
points_gained = 0
for i in range(tournaments_count):
    place = input()
    if place == 'W':
        points += 2000
        wins += 1
        points_gained += 2000
    elif place == 'F':
        points += 1200
        points_gained += 1200
    elif place == 'SF':
        points += 720
        points_gained += 720

wins_percentage = wins / tournaments_count * 100
average_points = points_gained / tournaments_count

print(f"Final points: {points}")
print(f"Average points: {floor(average_points)}")
print(f"{wins_percentage:.2f}%")
