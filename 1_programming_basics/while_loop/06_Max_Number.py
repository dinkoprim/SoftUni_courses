num = input()
biggest = int(num) - 1

while num != "Stop":
    num = int(num)
    if num > biggest:
        biggest = num
    num = input()

print(biggest)