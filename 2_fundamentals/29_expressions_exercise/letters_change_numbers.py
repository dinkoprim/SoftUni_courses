line = input().split()
result = 0

while line:
    el = line.pop()
    num = int(''.join(char for char in el if char.isdigit()))
    first_letter, last_letter = el[0], el[-1]
    first_letter_position = ord(first_letter.upper()) - 64
    last_letter_position = ord(last_letter.upper()) - 64

    if first_letter.isupper():
        num /= first_letter_position
    elif first_letter.islower():
        num *= first_letter_position

    if last_letter.isupper():
        num -= last_letter_position
    elif last_letter.islower():
        num += last_letter_position

    result += num

print(f'{result:.2f}')
