gifts_list = input().split(' ')
command = input()
while command != 'No Money':
    command = command.split(' ')
    action = command[0]
    gift = command[1]

    if action == 'OutOfStock':
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = 'None'
    elif action == 'Required':
        index = int(command[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = gift
    elif action == 'JustInCase':
        gifts_list.pop()
        gifts_list.append(gift)

    command = input()

for element in gifts_list:
    if element != 'None':
        print(element, end=' ')