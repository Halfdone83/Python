budget = float(input())
season = input()

total_cost = 0
destination = None
type = ""

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        type = "Camp"
        total_cost = budget * 0.30

    else:
        type = "Hotel"
        total_cost = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        type = "Camp"
        total_cost = budget * 0.40
    else:
        type = "Hotel"
        total_cost = budget * 0.80

else:
    destination = "Europe"
    type = "Hotel"
    total_cost = budget * 0.90


print(f" Somewhere in {destination}")
print(f" {type} - {total_cost:.2f}")

