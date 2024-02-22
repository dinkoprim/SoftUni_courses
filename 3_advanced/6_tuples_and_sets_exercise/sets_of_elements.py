# n, m = [int(x) for x in input().split()]
# n_set = set()
# m_set = set()
#
# for _ in range(n):
# 	n_set.add(int(input()))
#
# for _ in range(m):
# 	m_set.add(int(input()))
#
# print(*n_set.intersection(m_set), sep='\n')


n, m = [int(x) for x in input().split()]

n_set = set([input() for _ in range(n)])
m_set = set([input() for _ in range(m)])

print(*n_set.intersection(m_set), sep='\n')