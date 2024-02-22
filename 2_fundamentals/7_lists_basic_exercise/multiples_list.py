factor = int(input())
count = int(input())
count_list = []
for num in range(1, count+1):
    element = num * factor
    count_list.append(element)
print(count_list)
