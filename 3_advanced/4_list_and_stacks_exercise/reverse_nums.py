from collections import deque

line = deque(input().split())
reversed_line = deque(line.pop() for _ in range(len(line)))

print(' '.join(reversed_line))
