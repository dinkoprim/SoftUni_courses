initial_list = input().split('!')


def shopping(items_list):
    while True:
        command = input()
        if command == 'Go Shopping!':
            break
        command_parts = command.split(' ')
        action = command_parts[0]

        if action == 'Urgent':
            item = command_parts[1]
            if item not in items_list:
                items_list.insert(0, item)
        elif action == 'Unnecessary':
            item = command_parts[1]
            if item in items_list:
                items_list.remove(item)
        elif action == 'Correct':
            old_item = command_parts[1]
            new_item = command_parts[2]
            if old_item in items_list:
                items_list[items_list.index(old_item)] = new_item
        elif action == 'Rearrange':
            item = command_parts[1]
            if item in items_list:
                items_list.remove(item)
                items_list.append(item)

    print(', '.join(items_list))


run = shopping(initial_list)
