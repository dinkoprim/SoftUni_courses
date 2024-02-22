students_dict = {}
command = input()

while ":" in command:
	info = command.split(":")
	name, ID, course = info

	if course not in students_dict:
		students_dict[course] = {}
	students_dict[course][ID] = name
	command = input()

course = " ".join(command.split("_"))

for key, value in students_dict.items():
	if key == course:
		for ID, name in value.items():
			print(f'{name} - {ID}')

