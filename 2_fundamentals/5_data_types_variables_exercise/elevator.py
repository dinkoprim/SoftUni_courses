# n = int(input())
# p = int(input())
# courses_full = n // p
#
# if n % p != 0:
#     courses_full += 1
#
# print(round(courses_full))
#
from math import ceil
n = int(input())
p = int(input())
courses = ceil(n / p)
print(courses)