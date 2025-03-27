PEN_PRICE = 5.80
MARKERS_PRICE = 7.20
DETERGENT_PRICE = 1.20

total_pens = int(input())
total_markers = int(input())
total_detergent = int(input())
discount = int(input())

materials_price = \
    total_pens * PEN_PRICE +\
    total_markers * MARKERS_PRICE +\
    total_detergent * DETERGENT_PRICE

total_discount = materials_price * discount / 100

total_price = materials_price - total_discount

print(total_price)

