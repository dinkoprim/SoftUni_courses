import re

line = input()

while line:
    pattern = "\\d+"
    match = re.findall(pattern, line)
    if match:
        print(' '.join(match), end=' ')

    line = input()

