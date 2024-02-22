from collections import deque

legendary = {'Shadowmourne': 'shards',
             'Valanyr': 'fragments',
             'Dragonwrath': 'motes',
             }

materials = {'shards': 0,
             'fragments': 0,
             'motes': 0,
             }
junk = {}
collected = False

while True:
    line = deque(input().split())

    while line:
        qty = int(line.popleft())
        item = line.popleft().lower()

        if item in materials.keys():
            materials[item] += qty
        elif item in junk.keys():
            junk[item] += qty
        else:
            junk[item] = qty

        legend_item = next(
            (legend_item for legend_item, material in legendary.items() if materials[material] >= 250), None)

        if legend_item:
            collected = True
            print(f'{legend_item} obtained!')
            materials[legendary[legend_item]] -= 250
            break

    if collected:
        break

[print(f'{k}: {v}') for k, v in materials.items()]
[print(f'{k}: {v}') for k, v in junk.items()]
