budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_cost_percent = int(input())


total_cost = nights * price_per_night

if nights > 7:
    total_cost *= 0.95

additional_cost = budget / 100 * additional_cost_percent

budget_left = budget - additional_cost


if total_cost < budget_left:
    print(f"Ivanovi will be left with {budget_left - total_cost:.2f} leva after vacation.")
else:
    print(f"{total_cost - budget_left:.2f} leva needed.")