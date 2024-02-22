team_a = list(range(1,12))
team_b = list(range(1,12))
penalties_list = input().split()
new_penalty_list = []
for penalty in penalties_list:
    each_entry = penalty.split('-')
    new_penalty_list.append(each_entry)
for penalty in new_penalty_list:
    if 'A' in penalty:
        penalty.remove('A')
        penalty = int(penalty[0])
        if penalty not in team_a:
            continue
        else:
            team_a.remove(penalty)
    elif 'B' in penalty:
        penalty.remove('B')
        penalty = int(penalty[0])
        if penalty not in team_b:
            continue
        else:
            team_b.remove(penalty)
    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print(f"Game was terminated")
        break
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
