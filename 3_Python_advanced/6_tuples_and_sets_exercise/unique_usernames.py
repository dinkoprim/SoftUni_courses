# username_set = set()
# for _ in range(int(input())):
# 	username_set.add(input())
#
# print(*username_set, sep='\n')

# username_set = set([input() for _ in range(int(input()))])
# print(*username_set, sep='\n')

print(*set([input() for _ in range(int(input()))]), sep='\n')
