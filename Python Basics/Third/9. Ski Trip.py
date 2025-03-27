days = int(input())
room_type = input()
score = input()

nights = days - 1
total_price = 0

room_for_one_person_price = 18
apartment_price = 25
president_apartment = 35

if room_type == "room for one person":
    total_price = room_for_one_person_price * nights

elif room_type == "apartment":
    total_price = apartment_price * nights

    if nights < 10:
        total_price *= 0.70
    elif 10 < nights < 15:
        total_price *= 0.65
    elif nights > 15:
        total_price *= 0.50

elif room_type == "president apartment":
    total_price = president_apartment * nights

    if nights < 10:
        total_price *= 0.90
    elif 10 < nights < 15:
        total_price *= 0.85
    elif nights > 15:
        total_price *= 0.80


if score == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90


print (f'{total_price:.2f}')
