import os

input_path = os.path.join('..', 'resources', 'text.txt')
output_path = os.path.join('..', 'resources', 'output.txt')
chars_to_replace = ["-", ",", ".", "!", "?"]

with open(input_path) as text:
    lines = text.readlines()

even_lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]

with open(output_path, 'a') as output:
    for line in even_lines:
        words = line.split()
        reversed_line = ' '.join(reversed(words))

        for char in chars_to_replace:
            reversed_line = reversed_line.replace(char, '@')

        output.write(f'{reversed_line}\n')


