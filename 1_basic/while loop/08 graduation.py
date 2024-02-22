name = input()
counter_expel = 0
counter_year = 1
grades_total = 0
while True:
    grade = float(input())

    if grade < 4:
        counter_expel += 1
        if counter_expel > 1:
            print(f'{name} has been excluded at {counter_year} grade')
            break
        continue
    grades_total += grade
    counter_year += 1

    if counter_year > 12:
        print(f"{name} graduated. Average grade: {grades_total/12:.2f}")
        break
