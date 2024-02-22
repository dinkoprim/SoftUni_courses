string = input()
char = 0
for i in string:
    if i == 'a':
        char += 1
    elif i == 'e':
        char += 2
    elif i == 'i':
        char += 3
    elif i == 'o':
        char += 4
    elif i == 'u':
        char += 5
print(char)
