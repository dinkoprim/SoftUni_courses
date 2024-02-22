log = {}
n = int(input())
result = ''

for _ in range(n):
    name = str(input())
    grade = float(input())

    if name not in log.keys():
        log[name] = [grade]
    else:
        log[name].append(grade)

for name, grades in log.items():
    average = sum(grades) / len(grades)
    if average >= 4.50:
        result += f'{name} -> {average:.2f}\n'

print(result.strip())
