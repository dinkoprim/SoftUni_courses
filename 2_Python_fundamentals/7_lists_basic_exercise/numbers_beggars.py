offerings_string = input().split(', ')
offerings_integers = []
beggars_count = int(input())
offerings_distribution = []

for offering in offerings_string:
    offerings_integers.append(int(offering))

start_index = 0

while start_index < beggars_count:
    sum_for_beggar = 0
    for current_index in range(start_index, len(offerings_integers), beggars_count):
        sum_for_beggar += offerings_integers[current_index]  # МНОГО ВАЖНО !!!

    offerings_distribution.append(sum_for_beggar)
    start_index += 1

print(offerings_distribution)