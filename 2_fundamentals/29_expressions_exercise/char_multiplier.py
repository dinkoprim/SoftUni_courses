from collections import deque


def multiplier(str1, str2):
    total_sum = 0
    str1 = deque(str1)
    str2 = deque(str2)

    while str1 and str2:
        el1, el2 = ord(str1.popleft()), ord(str2.popleft())
        result = el1 * el2
        total_sum += result

    while str1:
        el = ord(str1.popleft())
        total_sum += el

    while str2:
        el = ord(str2.popleft())
        total_sum += el

    return print(total_sum)


str1, str2 = input().split()
multiplier(str1, str2)