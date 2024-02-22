total_rooms = int(input())
total_chairs = 0
total_visitors = 0
enough_chairs = True
for room in range(1, total_rooms + 1):

    command = input().split()
    chairs = int(len(command[0]))
    visitors = int(command[1])
    if chairs - visitors < 0:
        needed_chairs_in_room = visitors - chairs
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")
        enough_chairs = False
    total_chairs += chairs
    total_visitors += visitors
if enough_chairs:
    print(f"Game On, {total_chairs - total_visitors} free chairs left")