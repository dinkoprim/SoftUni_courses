import os


def get_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)

        if os.path.isfile(file_path):
            extension = filename.split('.')[-1]
            extensions[extension] = extensions.get(extension, []) + [filename]
        elif os.path.isdir(file_path) and not first_level:
            get_extensions(file_path, first_level=True)


output_path = os.path.join('..', 'resources', '4_report.txt')
directory = input('Enter directory you like to traverse: ')
extensions = {}
result = []

try:
    get_extensions(directory)
except FileNotFoundError:
    print('Directory not found!')

extensions = sorted(extensions.items(), key=lambda x: x[0])

for ext, files in extensions:
    result.append(f'.{ext}')
    for file in sorted(files):
        result.append(f'- - - {file}')

with open(output_path, 'w') as report:
    report.write('\n'.join(result))
