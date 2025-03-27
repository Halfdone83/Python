from math import  ceil , floor

X = int(input())
Y = float(input())
z = int(input())
workers = int(input())


harvest = X * Y
harvest_for_wine = harvest * 0.40
wine_liters = harvest_for_wine / 2.5

wine_left = abs(wine_liters - z)
wine_per_person = wine_left / workers

if wine_liters <= z:
    print(f"It will be a tough winter! More {floor(wine_left)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {ceil(wine_liters)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_per_person)} liters per person.")


