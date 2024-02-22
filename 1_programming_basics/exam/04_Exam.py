students_count = int(input())
group_1, group_2, group_3, group_4 = 0, 0, 0, 0
grades_total = 0
for i in range(1, students_count + 1):
    individual_grade = float(input())
    grades_total += individual_grade
    if individual_grade >= 5:
        group_1 += 1
    elif 4 <= individual_grade <= 4.99:
        group_2 += 1
    elif 3 <= individual_grade <= 3.99:
        group_3 += 1
    elif individual_grade < 3:
        group_4 += 1

group_1_percent = group_1 / students_count * 100
group_2_percent = group_2 / students_count * 100
group_3_percent = group_3 / students_count * 100
group_4_percent = group_4 / students_count * 100
average_grade = grades_total / students_count

print(f"Top students: {group_1_percent:.2f}%")
print(f"Between 4.00 and 4.99: {group_2_percent:.2f}%")
print(f"Between 3.00 and 3.99: {group_3_percent:.2f}%")
print(f"Fail: {group_4_percent:.2f}%")
print(f"Average: {average_grade:.2f}")

