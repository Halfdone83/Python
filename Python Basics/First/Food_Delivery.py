CHICKEN_PRICE = 10.35
FISH_PRICE = 12.40
VEGETERAIN_PRICE =  8.15
DELIVERY_PRICE = 2.50

chicken_menus = int(input())
fish_menus = int(input())
vegeterain_menus = int(input())

menus_price = \
    CHICKEN_PRICE * chicken_menus +\
    FISH_PRICE * fish_menus +\
    VEGETERAIN_PRICE * vegeterain_menus \

desserts_price = menus_price * 0.20

total_price = menus_price + desserts_price + DELIVERY_PRICE

print(total_price)