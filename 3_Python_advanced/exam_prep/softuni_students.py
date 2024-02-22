def softuni_students(*course_code_username_pair, **course_code_course_name_pair):
    result = []
    invalid_students = set()
    successful_students = {}

    for course_code, username in course_code_username_pair:
        if course_code in course_code_course_name_pair.keys():
            course_name = course_code_course_name_pair[course_code]
            successful_students[username] = course_name
        else:
            invalid_students.add(username)

    sorted_successful_students = sorted(successful_students.items())

    for student_name, course_name in sorted_successful_students:
        result.append(f"*** A student with the username {student_name} has successfully finished the course {course_name}!")
    if invalid_students:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid_students))}")

    return '\n'.join(result)


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))




