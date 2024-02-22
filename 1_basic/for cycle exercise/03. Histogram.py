p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

n = int(input())

for i in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    else:
        p5 += 1

p1_percent = p1 * 100 / n
p2_percent = p2 * 100 / n
p3_percent = p3 * 100 / n
p4_percent = p4 * 100 / n
p5_percent = p5 * 100 / n

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')
