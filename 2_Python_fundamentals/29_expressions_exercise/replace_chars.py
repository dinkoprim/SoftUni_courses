line = input()
pure_line = ""
for i, char in enumerate(line):
    if i+1 != len(line):
        if char != line[i + 1]:
            pure_line += char
pure_line += line[-1]
print(pure_line)
