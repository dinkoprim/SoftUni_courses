line = input()
strength = 0
result = ''

for i in range(len(line)):
    if strength > 0 and line[i] != '>':
        strength -= 1
    elif line[i] == '>':
        result += '>'
        strength += int(line[i+1])
    else:
        result += line[i]

print(result)