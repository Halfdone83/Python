NYLON_PRICE = 1.50
PAINT_PRICE = 14.5
THINNER_PRICE = 5
BAGS_PRICE = 0.40

nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

total_nylon = nylon * NYLON_PRICE
total_paint = paint * PAINT_PRICE
total_thinner = thinner * THINNER_PRICE

nylon = total_nylon + 2
paint = total_paint + total_paint * 0.10


total_materials_price = total_nylon + total_paint + total_thinner
workers_payment = total_materials_price + total_materials_price * 0.30

total_payment = total_materials_price + workers_payment

print (total_payment)
