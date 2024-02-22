def happiness_calc(list_of_employees, multiplier):
    employees_happiness = [int(num) * multiplier for num in list_of_employees]
    total_count = len(employees_happiness)
    average_happiness = sum(employees_happiness) / total_count
    happy_count = len(list(filter(lambda x: x >= average_happiness, employees_happiness)))
    message = f'Employees are happy!' if happy_count >= total_count / 2\
        else f'Employees are not happy!'
    return f'Score: {happy_count}/{total_count}. {message}'


happiness = input().split()
factor = int(input())
print(happiness_calc(happiness, factor))
