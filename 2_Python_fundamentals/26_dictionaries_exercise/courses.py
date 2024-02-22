result = ''
log = {}

line = input()
while line != 'end':
    course, student = line.split(' : ')

    if course not in log:
        log[course] = []
    log[course].append(student)

    line = input()

for k, v in log.items():
    result += f'{k}: {len(v)}\n'
    for name in v:
        result += f'-- {name}\n'

print(result)
