import os

path = os.path.join('..', 'resources')

line = input()

while line != 'End':
    cmd, *info = line.split('-')
    file_path = os.path.join(path, info[0])

    if cmd == 'Create':
        with open(file_path, 'w') as file:
            pass

    elif cmd == 'Add':
        with open(file_path, 'a') as file:
            file.write(f'{info[1]}\n')

    elif cmd == 'Replace':
        try:
            with open(file_path, 'r+') as file:
                text = file.read()
                text = text.replace(info[1], info[2])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif cmd == 'Delete':
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")

    line = input()
