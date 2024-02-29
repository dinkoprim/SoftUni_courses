raw_password = input()
reset_commands = []
while True:
    action = input()
    if action == "Done":
        break
    reset_commands.append(action)


def password_reset(raw_pass, commands):
    password = raw_pass

    for element in commands:
        tokens = element.split()

        if tokens[0] == 'TakeOdd':
            password = password[1::2]
            print(password)

        elif tokens[0] == 'Cut':
            index = int(tokens[1])
            length = int(tokens[2])
            substring = password[index:index + length]
            password = password[:index] + password[index + length:]
            print(password)

        elif tokens[0] == 'Substitute':
            substring = tokens[1]
            substitute = tokens[2]
            if substring in password:
                password = password.replace(substring, substitute)
                print(password)
            else:
                print("Nothing to replace!")

    return password


result = password_reset(raw_password, reset_commands)
print(f"Your password is: {result}")
