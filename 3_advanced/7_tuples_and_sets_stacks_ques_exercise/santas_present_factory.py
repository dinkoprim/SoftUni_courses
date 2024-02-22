from collections import deque

materials = [int(x) for x in input().split()]
magic_lvl = deque(int(x) for x in input().split())
toys_crafted = []
product = 0

presents = {
    'Doll':	150,
    'Wooden train':	250,
    'Teddy bear': 300,
    'Bicycle': 400,
}

while materials and magic_lvl:

    current_material = materials.pop() if magic_lvl[0] or not materials[-1] else 0
    current_magic = magic_lvl.popleft() if current_material or not magic_lvl[0] else 0

    if not current_magic:
        continue

    product = current_material * current_magic

    if product in presents.values():
        for key, value in presents.items():
            if value == product:
                toys_crafted.append(key)

    elif product < 0:
        materials.append(current_material + current_magic)

    elif product > 0:
        materials.append(current_material + 15)

    product = 0

if {"Doll", "Wooden train"}.issubset(toys_crafted) or {"Teddy bear", "Bicycle"}.issubset(toys_crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magic_lvl:
    print(f"Magic left: {', '.join(map(str, magic_lvl))}")

[print(f"{toy}: {toys_crafted.count(toy)}") for toy in sorted(set(toys_crafted))]
