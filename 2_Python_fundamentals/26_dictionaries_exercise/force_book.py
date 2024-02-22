result = ''
log = {}

line = input()
while line != 'Lumpawaroo':

    if '|' in line:
        side, user = line.split(' | ')
        cmd = '|'
    elif '->' in line:
        user, side = line.split(' -> ')
        cmd = '->'

    if side not in log.keys():
        log[side] = []

    if cmd == '|':

        if all(user not in lst for lst in log.values()):
            log[side].append(user)

    elif cmd == '->':

        for listed_users in log.values():
            if user in listed_users:
                listed_users.remove(user)
                log[side].append(user)
                print(f"{user} joins the {side} side!")
                break
        else:
            log[side].append(user)
            print(f"{user} joins the {side} side!")

    line = input()

for force, lst_users in log.items():
    if lst_users:
        result += f'Side: {force}, Members: {len(lst_users)}\n'
        for user in lst_users:
            result += f'! {user}\n'

print(result.strip())
