electrons = int(input())
result = []
shell_number = 1

while electrons > 0:
    shells_capacity = 2 * shell_number ** 2

    if electrons >= shells_capacity:
        result.append(shells_capacity)
        electrons -= shells_capacity
    else:
        result.append(electrons)
        break

    shell_number += 1

print(result)