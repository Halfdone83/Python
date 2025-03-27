fat_percent = int(input())
protein_percent = int(input())
carbohydrates = int(input())
total_calories = int(input())
water_percent = int(input())


total_fat = (fat_percent / 100 * total_calories) / 9

total_protein = (protein_percent / 100 * total_calories) / 4

total_carbohydrates = (carbohydrates / 100 * total_calories) / 4

total_food_weight = total_carbohydrates + total_protein + total_fat

calories_per_gram = total_calories / total_food_weight

real_calories = calories_per_gram - (calories_per_gram * water_percent / 100)

print(f'{real_calories:.4f}')
