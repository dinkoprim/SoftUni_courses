def loading_bar(some_number):
    empty_bar = []
    index = 0
    for num in range(10, some_number + 10, 10):
        empty_bar.append('%')
        index += 1
    empty_slots = 10 - index
    empty_bar.append('.'*empty_slots)
    if some_number < 100:
        return f"{user_number}% [{''.join(empty_bar)}]\nStill loading..."
    return f"100% Complete!\n[{''.join(empty_bar)}]"


user_number = int(input())
print(loading_bar(user_number))