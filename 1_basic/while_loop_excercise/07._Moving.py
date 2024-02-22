width = int(input())
length = int(input())
height = int(input())
user_input = input()

space = width * length * height
box_counter = 0
no_more_space = False

while user_input != 'Done':
    user_input = int(user_input)
    box_counter += user_input

    if box_counter >= space:
        no_more_space = True
        break
    user_input = input()

if no_more_space:
    print(f"No more free space! You need {box_counter - space} Cubic meters more.")
else:
    print(f"{space - box_counter} Cubic meters left.")


