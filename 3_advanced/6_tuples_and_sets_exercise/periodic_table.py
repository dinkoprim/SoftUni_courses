# elements_set = set()
#
# for _ in range(int(input())):
# 	elements = input().split()
# 	elements_set.update(elements)
#
# print(*elements_set, sep='\n')

elements_set = set()

[elements_set.update(input().split()) for _ in range(int(input()))]

print(*elements_set, sep='\n')