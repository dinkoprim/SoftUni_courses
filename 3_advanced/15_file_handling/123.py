import os.path

file_name = 'some_numbers.txt'
ABS_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
path = os.path.join(ABS_DIR_PATH, 'resources', file_name)

# file = open(path)

with open(path) as file:
    lines = file.readlines()

# file.close()
total = 0
for line in lines:
    line_as_int = int(line.strip())
    print(f'num: {line_as_int}')
    result = line_as_int + total
    print(f'{total} + {line_as_int} = {result}')
    total += line_as_int




print(total)