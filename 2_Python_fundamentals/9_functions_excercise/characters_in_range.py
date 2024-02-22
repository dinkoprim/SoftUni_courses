
def characters_finder(first, second):
    characters = []
    for chars_as_digits in range(ord(first) + 1, ord(second)):
        characters.append(chr(chars_as_digits))
    return characters


first_char = input()
second_char = input()
result = characters_finder(first_char, second_char)
print(*result)