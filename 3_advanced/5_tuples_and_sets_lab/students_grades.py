students_count = int(input())
students_record = {}
while students_count:
	name, grade = input().split()
	if name not in students_record:
		students_record[name] = [float(grade)]
	else:
		students_record[name].append(float(grade))
	students_count -= 1

for name, grades in students_record.items():
	average = sum(grades) / len(grades)
	grades_formatted = " ".join(f"{grade:.2f}" for grade in grades)
	print(f"{name} ->", f"{grades_formatted}", f"(avg: {average:.2f})")
