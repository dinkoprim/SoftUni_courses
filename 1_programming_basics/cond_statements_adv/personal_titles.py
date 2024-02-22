# input
age = float(input())
gender = str(input())
# logic
if age >= 16:
    if gender == 'm':
        result = 'Mr.'
    elif gender == 'f':
        result = 'Ms.'
elif age < 16:
    if gender == 'm':
        result = 'Master'
    elif gender == 'f':
        result = 'Miss'
# output
print(result)
