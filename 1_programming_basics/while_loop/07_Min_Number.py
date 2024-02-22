num = input()
smallest = int(num) + 1
while num != 'Stop':
    num = int(num)
    if num < smallest:
        smallest = num
    num = input()
print(smallest)
