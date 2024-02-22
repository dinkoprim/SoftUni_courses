from collections import deque
substrings = deque(input().split())

found_colors = []
all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}

secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

while substrings:
    left_side = substrings.popleft()
    right_side = substrings.pop() if substrings else ''

    for color in (left_side + right_side, right_side + left_side):
        if color in all_colors:
            found_colors.append(color)
            break
    else:
        for el in (left_side[:-1], right_side[:-1]):
            if el:
                substrings.insert(len(substrings)//2, el)

for color in set(secondary_colors.keys()).intersection(found_colors):
    if not secondary_colors[color].issubset(found_colors):
        found_colors.remove(color)

print(found_colors)