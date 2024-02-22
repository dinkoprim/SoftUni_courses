import random
counter = 0
for i in range(100):
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    if a and b == 6:
        counter += 1
dice = a + b
print(counter)
