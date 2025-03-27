MONEY_INCREASE = 10

age = int(input())
washing_machine = float(input())
toy_price = int(input())

money_given = 10
birthday_money = 0
birthday_toys = 0

for age in range(1, age + 1):
    if age % 2 == 0:
        birthday_money += money_given -1
        money_given += MONEY_INCREASE
    else:
        birthday_toys += 1

money_from_toys = birthday_toys * toy_price

total_money = birthday_money + money_from_toys

if total_money >= washing_machine:
    print(f"Yes {total_money - washing_machine:.2f}")
else:
    print(f'No {washing_machine - total_money:.2f}')