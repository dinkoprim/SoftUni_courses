line = input().split()
result = {}

for el in line:
    for c in el:
        if c not in result.keys():
            result[c] = 0
        result[c] += 1

[print(f'{k} -> {v}') for k, v in result.items()]