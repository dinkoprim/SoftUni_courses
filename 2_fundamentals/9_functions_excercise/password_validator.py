def validator(password):
    error_message = ''
    digit_count = 0

    if not 6 <= len(password) <= 10:
        error_message += f'Password must be between 6 and 10 characters\n'

    for char in password:
        if ord(char) not in range(48, 58) and ord(char) not in range(65, 91) and ord(char) not in range(97, 123):
            error_message += f"Password must consist only of letters and digits\n"
            break
        if ord(char) in range(48, 58):
            digit_count += 1

    if digit_count < 2:
        error_message += f"Password must have at least 2 digits"

    if not error_message:
        return f"Password is valid"
    else:
        return error_message


user_password = input()
print(validator(user_password))