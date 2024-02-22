max_fails = int(input())

user_input = input()
last_problem = ''
fail_counter = 0
grades_total = 0
problem_counter = 0

while user_input != 'Enough':
    last_problem = user_input
    grade = int(input())
    if grade <= 4:
        fail_counter += 1
    problem_counter += 1
    grades_total += grade
    if fail_counter >= max_fails:
        break

    user_input = input()

if fail_counter == max_fails:
    print(f"You need a break, {fail_counter} poor grades.")
else:
    print(f'Average score: {grades_total / problem_counter:.2f}')
    print(f'Number of problems: {problem_counter}')
    print(f"Last problem: {last_problem}")
