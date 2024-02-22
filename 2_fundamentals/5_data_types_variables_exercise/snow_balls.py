number_of_snowballs = int(input())
best_weight = 0
best_time = 0
best_value = 0
best_quality = 0

for snowball in range(1, number_of_snowballs+1):
    weight = int(input())
    air_time = int(input())
    quality = int(input())
    snowball_value = (weight / air_time) ** quality
    if snowball_value > best_value:
        best_value = snowball_value
        best_weight = weight
        best_time = air_time
        best_quality = quality

print(f"{best_weight} : {best_time} = {int(best_value)} ({best_quality})")