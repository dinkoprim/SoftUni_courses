group_count = int(input())
total_ppl = 0
group_5 = 0
group_6_12 = 0
group_13_25 = 0
group_26_40 = 0
group_41 = 0

for i in range(group_count):
    ppl_in_group = int(input())
    total_ppl += ppl_in_group
    if 1 <= ppl_in_group <= 5:
        group_5 += ppl_in_group
    elif 6 <= ppl_in_group <= 12:
        group_6_12 += ppl_in_group
    elif 13 <= ppl_in_group <= 25:
        group_13_25 += ppl_in_group
    elif 26 <= ppl_in_group <= 40:
        group_26_40 += ppl_in_group
    elif 41 <= ppl_in_group:
        group_41 += ppl_in_group

print(f'{group_5 / total_ppl * 100:.2f}%')
print(f'{group_6_12 / total_ppl * 100:.2f}%')
print(f'{group_13_25 / total_ppl * 100:.2f}%')
print(f'{group_26_40 / total_ppl * 100:.2f}%')
print(f'{group_41 / total_ppl * 100:.2f}%')
