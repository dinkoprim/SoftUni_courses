def gather_credits(credits_needed, *course_credit_pairs):
    enrolled_courses = []
    gathered_credits = 0

    for course, credits_scored in course_credit_pairs:
        if course not in enrolled_courses:
            enrolled_courses.append(course)
            credits_needed -= credits_scored
            gathered_credits += credits_scored

        if credits_needed <= 0:
            break
    if credits_needed <= 0:
        return (f"Enrollment finished! Maximum credits: {gathered_credits}.\n"
                f"Courses: {', '.join(sorted(enrolled_courses))}")

    return f"You need to enroll in more courses! You have to gather {credits_needed} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))



