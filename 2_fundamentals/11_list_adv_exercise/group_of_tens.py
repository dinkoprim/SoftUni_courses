sequence = [int(num) for num in input().split(', ')]
current_group = 10
while sequence:
    current_group_filter = [number for number in sequence if number <= current_group]
    print(f"Group of {current_group}'s: {current_group_filter}")
    current_group += 10
    sequence = [number for number in sequence if number not in current_group_filter]