line = input()
for i, char in enumerate(line):
    if char == ':':
        print(char + line[i+1])
