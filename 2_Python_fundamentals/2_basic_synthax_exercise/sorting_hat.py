name = input()
voldemort = False
while name != "Welcome!":
    if name == "Voldemort":
        voldemort = True
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()

if voldemort:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")