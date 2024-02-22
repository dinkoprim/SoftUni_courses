max_fails = int(input())
user_input = input()

last_problem = ''
problem_counter = 0
fail_counter = 0
grade_total = 0

while user_input != 'Enough':
    last_problem = user_input
    grade = int(input())
    grade_total += grade
    problem_counter += 1
    if grade <= 4:
        fail_counter += 1
        if fail_counter >= max_fails:
            print(f"You need a break, {fail_counter} poor grades.")
            break

    user_input = input()
if fail_counter != max_fails:
    print(f'Average score: {grade_total / problem_counter:.2f}')
    print(f'Number of problems: {problem_counter}')
    print(f"Last problem: {last_problem}")
