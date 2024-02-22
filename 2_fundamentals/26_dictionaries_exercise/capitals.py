#
# countries = input().split(', ')
# capitals = input().split(', ')
#
# info = dict(zip(countries, capitals))
#
# [print(f'{force} -> {v}') for force, v in info.items()]

[print(f'{name} -> {capital}') for name, capital in dict(zip(input().split(', '), input().split(', '))).items()]

# print('\n'.join([f'{name} -> {capital}' for name, capital in zip(input().split(', '), input().split(', '))]))

# Bulgaria, Germany, France
# Varna, Frankfurt, Paris