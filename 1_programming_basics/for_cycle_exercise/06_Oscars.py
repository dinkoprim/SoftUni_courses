actor_name = str(input())
academy_points = float(input())
jury_members = int(input())
nomination_score_reached = False
overall_score = 0


for i in range(jury_members):
    jury_member_name = str(input())
    jury_score = float(input())
    added_points = len(jury_member_name) * jury_score / 2
    academy_points += added_points
    if academy_points > 1250.5:
        nomination_score_reached = True
        break
if nomination_score_reached:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!")

