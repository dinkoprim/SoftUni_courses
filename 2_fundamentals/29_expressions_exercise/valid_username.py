def username_length(username):
    if len(username) in range(3, 17):
        return True
    return False


def username_chars_are_valid(username):
    allowed_symbols = ['-', '_']
    if all(char.isalnum() or char in allowed_symbols for char in username):
        return True
    return False


def username_is_valid(username):
    if username_length(username) and username_chars_are_valid(username):
        return True
    return False


line = input().split(', ')
valid_names = []
for username in line:
    if username_is_valid(username):
        valid_names.append(username)

print('\n'.join(valid_names))



# def valid_names(usernames):
#     valids = []
#     allowed_symbols = ['-', '_']
#
#     for name in usernames:
#         if len(name) in range(3, 17):
#             if all(char.isalnum() or char in allowed_symbols for char in name):
#                 valids.append(name)
#
#     return '\n'.join(valids)
#
#
# line = input().split(', ')
# print(valid_names(line))
