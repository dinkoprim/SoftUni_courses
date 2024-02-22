from collections import deque


worms_stack = [int(x) for x in input().split()]
holes_que = deque(int(x) for x in input().split())
matches = 0
worms_count = len(worms_stack)

while worms_stack and holes_que:
    worm = worms_stack.pop()
    hole = holes_que.popleft()

    if worm <= 0:
        holes_que.appendleft(hole)
        continue

    if worm != hole:
        worm -= 3
        worms_stack.append(worm)
    else:
        matches += 1


if matches:
    print(f"Matches: {matches}")
else:
    print(f"There are no matches.")

if not worms_stack:
    if worms_count == matches:
        print(f"Every worm found a suitable hole!")
    else:
        print(f"Worms left: none")
else:
    print(f"Worms left: {', '.join([str(worm) for worm in worms_stack])}")

if not holes_que:
    print(f"Holes left: none")
else:
    print(f"Holes left: {', '.join([str(hole) for hole in holes_que])}")

