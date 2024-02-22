def team_lineup(*player_country_pairs):
    lineup = {}

    for player, country in player_country_pairs:
        if country not in lineup.keys():
            lineup[country] = [player]
        else:
            lineup[country].append(player)

    sorted_lineup = {k: v for k, v in sorted(lineup.items(), key=lambda item: (-len(item[1]), item[0]))}

    result = f''
    for country, players in sorted_lineup.items():
        result += f"\n{country}:\n  -{'\n  -'.join(players)}"

    return result.strip()

    # result = ''
    # for country, players in sorted_lineup.items():
    #     result += f'{country}:\n'
    #     for player in players:
    #         result += f'  -{player}\n'


    # result = '\n'.join(
    #     [f"{country}:" + ''.join([f"\n  -{player}" for player in players]) for country, players in sorted_lineup.items()])
    #
    # return result.strip('\n')


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

