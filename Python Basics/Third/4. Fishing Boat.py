budget = int(input())
season = input()
fishers = int(input())


total_price = 0

if season == "Spring":
    total_price = 3000

    if fishers <= 6:
        total_price *= 0.90
    elif 7 <= fishers <= 11:
        total_price *= 0.85
    else:
        total_price *= 0.75

elif season == "Summer":
    total_price = 4200

    if fishers <= 6:
        total_price *= 0.90
    elif 7 <= fishers <= 11:
        total_price *= 0.85
    else:
        total_price *= 0.75

elif season == "Autumn":
    total_price = 4200

    if fishers <= 6:
        total_price *= 0.90
    elif 7 <= fishers <= 11:
        total_price *= 0.85
    else:
        total_price *= 0.75

elif season == "Winter":
    total_price = 2600

    if fishers <= 6:
        total_price *= 0.90
    elif 7 <= fishers <= 11:
        total_price *= 0.85
    else:
        total_price *= 0.75

if season != "Autumn" and fishers % 2 == 0:
    total_price *= 0.95

if budget >= total_price:
    print(f" Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")