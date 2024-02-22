log = {}
result = ''
while True:
    line = input()

    if line == 'End':
        break

    company, id_no = line.split(' -> ')
    if company not in log.keys():
        log[company] = []

    if id_no not in log[company]:
        log[company].append(id_no)

for k, v in log.items():
    result += f'{k}\n'
    for i in v:
        result += f'-- {i}\n'

print(result.strip())