def age_assignment(*names, **kwargs):
    name_age = {}
    for letter, age in kwargs.items():
        for name in names:
            if name.startswith(letter):
                name_age[name] = age

    name_age = sorted(name_age.items(), key=lambda x: x[0])
    return '\n'.join(f"{name} is {age} years old." for name, age in name_age)


print(age_assignment("Peter", "George", G=26, P=19))