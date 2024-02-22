text = input()
cyphered = ""
for char in text:
    new_char = ord(char) + 3
    cyphered += chr(new_char)

print(cyphered)
