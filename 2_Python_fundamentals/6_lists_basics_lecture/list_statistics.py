number_of_int = int(input())
positives_list = []
negatives_list = []
positives_count = 0
negatives_sum = 0
for _ in range(number_of_int):
    number = int(input())
    if number > 0:
        positives_count += 1
        positives_list.append(number)
    else:
        negatives_sum += number
        negatives_list.append(number)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {positives_count}")
print(f"Sum of negatives: {negatives_sum}")