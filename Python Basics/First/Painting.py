NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5
BAGS_PRICE = 0.40

nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())

nylon += 2
paint += paint * 0.10

nylon_needed = nylon * NYLON_PRICE
paint_needed = paint * PAINT_PRICE
thinner_needed = thinner * THINNER_PRICE

materials_price = \
    nylon_needed + \
    paint_needed + \
    thinner_needed + \
    BAGS_PRICE

working_pay_per_hour = materials_price * 0.30
workers_total_pay = working_pay_per_hour * working_hours

total_price = materials_price + workers_total_pay

print(total_price)