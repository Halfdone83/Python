degreese = int(input())
time_of_day = input()

Shoes = None
Outfit = None

if 10 <= degreese <= 18:
    if time_of_day == 'Morning':
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif time_of_day == 'Afternoon':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

elif 18 < degreese <= 24:
    if time_of_day == 'Morning':
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif time_of_day == 'Afternoon':
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

else:
    if time_of_day == 'Morning':
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif time_of_day == 'Afternoon':
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"


print(f" It's {degreese} degrees, get your {Outfit} and {Shoes}.")