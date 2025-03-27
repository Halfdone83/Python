budget = float(input())
extras = int(input())
clothing_price = float(input())


decor_price = budget * 0.10


if extras > 150:
    clothing_price = clothing_price * 0.90


total_cost = \
    extras * \
    clothing_price + \
    decor_price


if total_cost <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")

