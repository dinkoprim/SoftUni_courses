import os

file_name = 'some_numbers.txt'
path = os.path.join('..', 'resources', file_name)
ABS_DIR_PATH = os.path.abspath(__file__)

try:
    file = open(path)
    print('file found')
    print(file.read())
except FileNotFoundError:
    print('file not found')