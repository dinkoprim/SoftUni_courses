sequence = input().split(' ')
absolute_value = []

for num in sequence:
    absolute_value.append(abs(float(num)))

print(absolute_value)