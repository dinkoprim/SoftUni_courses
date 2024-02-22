tabs_open = int(input())
salary = float(input())
flag = False
for i in range(tabs_open):
    tab_name = str(input())
    if tab_name == 'Facebook':
        salary -= 150
    elif tab_name == 'Instagram':
        salary -= 100
    elif tab_name == 'Reddit':
        salary -= 50
    if salary <= 0:
        flag = True
        break
if flag:
    print("You have lost your salary.")
else:
    print(f'{salary:.0f}')