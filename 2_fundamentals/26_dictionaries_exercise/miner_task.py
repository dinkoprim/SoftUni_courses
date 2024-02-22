result = {}

while True:
    line = input()
    if line == 'stop':
        break

    material = line
    quantity = int(input())

    if material not in result.keys():
        result[material] = 0
    result[material] += quantity

[print(f'{k} -> {v}') for k, v in result.items()]