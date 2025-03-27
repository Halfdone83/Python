excursion_price = float(input())

PUZZELS_PRICE = 2.60
DOLLS_PRICE = 3
BEARS_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

final_price = 0
profit = 0

puzzels_total = int(input())
dolls_total = int(input())
bears_total = int(input())
minions_total = int(input())
trucks_total = int(input())


total_price = \
    puzzels_total * PUZZELS_PRICE + \
    dolls_total * DOLLS_PRICE + \
    bears_total * BEARS_PRICE + \
    minions_total * MINION_PRICE + \
    trucks_total * TRUCK_PRICE \


total_toys = \
        puzzels_total + \
        dolls_total + \
        bears_total + \
        minions_total + \
        trucks_total


if total_toys >= 50:
    final_price = total_price * 0.75
else:
    final_price = total_price

profit = final_price - final_price * 0.10

if profit >= excursion_price:
    print(f"Yes! {profit - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {abs(excursion_price - profit):.2f} lv needed.")