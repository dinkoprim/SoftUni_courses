import os
import string

input_path = os.path.join('..', 'resources', 'text.txt')
output_path = os.path.join('..', 'resources', 'output.txt')

with open(input_path) as text:
    lines = text.readlines()

with open(output_path, 'w') as output:
    for i, row in enumerate(lines, start=1):
        row = row.replace('\n', '')
        el_in_row = row.split()

        flattened_symbols = [char for word in el_in_row for char in word]
        chr_count = sum(1 for char in flattened_symbols if char.isalpha())
        punctuation_count = sum(1 for char in flattened_symbols if char in string.punctuation)

        modified_row = f'Line {i}: {row} ({chr_count})({punctuation_count})'

        output.write(f"{modified_row}\n")