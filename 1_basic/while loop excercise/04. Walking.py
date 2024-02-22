user_input = input()
total_steps = 0
goal = 10000

while user_input != "Going home":
    steps = int(user_input)
    total_steps += steps
    if total_steps >= goal:
        break
    user_input = input()

if user_input == "Going home":
    walk_home = int(input())
    total_steps += walk_home
diff = abs(total_steps - goal)
if total_steps < goal:
    print(f"{diff} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
