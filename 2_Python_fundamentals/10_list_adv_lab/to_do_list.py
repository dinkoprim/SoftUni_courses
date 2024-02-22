def to_do_notes(command):
    notes_list = [0 for i in range(100)]
    while True:
        if command == 'End':
            break
        importance = int(command.split('-')[0]) - 1
        notes_list.pop(importance)
        notes_list.insert(importance, command.split('-')[1])

        command = input()
    return list(filter(lambda x: x != 0, notes_list))


user_command = input()
print(to_do_notes(user_command))
