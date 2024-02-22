import os
import re

words_path = os.path.join('..', 'resources', 'words.txt')
input_path = os.path.join('..', 'resources', 'input.txt')
output_path = os.path.join('..', 'resources', 'output.txt')

with open(words_path) as words:
    searched_words_text = words.read()
    searched_words_list = [word.lower() for word in searched_words_text.split()]

with open(input_path) as text:
    content = text.read().lower()

words_count = {}

for word in searched_words_list:
    pattern = re.compile(rf'\b{word}\b')
    result = re.findall(pattern, content)
    words_count[word] = len(searched_words_list)

sorted_words_count = sorted(words_count.items(), key=lambda x: -x[1])

with open(output_path, 'a') as output:
    for word, count in sorted_words_count:
        output.write(f'{word} - {count}\n')
