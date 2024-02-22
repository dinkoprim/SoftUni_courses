from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

items = {'Patch': 30, 'Bandage': 40, 'MedKit': 100}
inventory = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}

while textiles and medicaments:
    fabric = textiles.popleft()
    drug = medicaments.pop()
    attempt = fabric + drug

    if attempt in items.values():
        for item, val in items.items():
            if attempt == val:
                inventory[item] += 1
                break

    elif attempt > items['MedKit']:
        inventory['MedKit'] += 1
        attempt -= items['MedKit']
        medicaments[-1] += attempt
    else:
        drug += 10
        medicaments.append(drug)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print("Textiles are empty.")
    elif not medicaments:
        print("Medicaments are empty.")

inventory = dict(sorted(inventory.items(), key=lambda x: (-x[1], x[0])))

result = ''
for k, v in inventory.items():
    if v:
        result += f'{k} - {v}\n'

print(result.strip())
if medicaments:
    print(f'Medicaments left: ' + ', '.join(str(x) for x in reversed(medicaments)))
if textiles:
    print(f'Textiles left: ' + ', '.join(str(x) for x in textiles))
