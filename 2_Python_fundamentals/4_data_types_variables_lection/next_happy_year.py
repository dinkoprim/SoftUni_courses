input_year = int(input())
while True:
    input_year += 1
    year_str = str(input_year)
    if len(set(year_str)) == len(year_str):
        break
print(input_year)