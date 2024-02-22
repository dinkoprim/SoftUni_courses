result = {}

while True:
    line = input()
    if line.isdigit():
        break
    name, number = line.split('-')
    result[name] = number

for _ in range(int(line)):
    searched_name = input()
    if searched_name not in result.keys():
        print(f"Contact {searched_name} does not exist.")
        continue
    print(f'{searched_name} -> {result[searched_name]}')

