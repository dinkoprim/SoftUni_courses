fat_percentage = int(input()) / 100
proteins_percentage = int(input()) / 100
carbs_percentage = int(input()) / 100
total_calories = int(input())
water_percentage = 1 - (int(input()) / 100)

grams_of_fat = fat_percentage * total_calories / 9
grams_of_proteins = proteins_percentage * total_calories / 4
grams_of_carbs = carbs_percentage * total_calories / 4
total_grams = grams_of_fat + grams_of_proteins + grams_of_carbs
calories_per_gram_with_water = total_calories / total_grams
calories_per_gram = calories_per_gram_with_water * water_percentage
print(f'{calories_per_gram:.4f}')
