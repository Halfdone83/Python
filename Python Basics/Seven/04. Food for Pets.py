days = int(input())
total_food = float(input())

total_food_eaten = 0
dog_eaten = 0
cat_eaten = 0
biscuits = 0


for i in range(1, days + 1):
    dog = int(input())
    cat = int(input())

    both_per_day = dog + cat

    dog_eaten += dog
    cat_eaten += cat

    if i % 3 == 0:
        biscuits += both_per_day * 0.10

    total_food_eaten = dog_eaten + cat_eaten

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food_eaten / total_food * 100:.2f}% of the food has been eaten.")
print(f"{dog_eaten / total_food_eaten * 100:.2f}% eaten from the dog.")
print(f"{cat_eaten / total_food_eaten * 100:.2f}% eaten from the cat.")
