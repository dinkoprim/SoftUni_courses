import re

n = int(input())

for _ in range(n):
    text = input()
    regex = r'((?P<start>[\*@]))(?P<tag>[A-Z][a-z]{2,})(\2:[ ])(\[(?P<letter_1>[A-Za-z])\])\|' \
            r'(\[(?P<letter_2>[A-Za-z])\])\|(\[(?P<letter_3>[A-Za-z])\])\|$'
    match = re.search(regex, text)
    if match:
        tag = match.group('tag')
        letter_1 = match.group('letter_1')
        letter_2 = match.group('letter_2')
        letter_3 = match.group('letter_3')
        stuff = f'{letter_1}{letter_2}{letter_3}'
        print(f'{tag}:', end=' ')
        print(' '.join([str(ord(x)) for x in stuff]))
    else:
        print('Valid message not found!')