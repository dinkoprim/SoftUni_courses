type_of_fire = input().split('#')
water_left = int(input())
total_effort = 0
cells_extinguished = []

low = range(1, 51)
medium = range(51, 81)
high = range(81, 126)

for fires in type_of_fire:
    fire_level, cell_value = fires.split(' = ')
    cell_value = int(cell_value)
    is_fire_within_range = False
    is_water_enough = True
    if fire_level == 'High' and cell_value in high:
        is_fire_within_range = True
    elif fire_level == 'Medium' and cell_value in medium:
        is_fire_within_range = True
    elif fire_level == 'Low' and cell_value in low:
        is_fire_within_range = True
    if cell_value > water_left:
        is_water_enough = False
    if is_fire_within_range and is_water_enough:
        water_left -= cell_value
        total_effort += cell_value * 0.25
        cells_extinguished.append(cell_value)

print(f'Cells:')
for cells in range(len(cells_extinguished)):
    print(f' - {cells_extinguished[cells]}')
print(f'Effort: {total_effort:.2f}')
print(f"Total Fire: {sum(cells_extinguished)}")
