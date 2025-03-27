strawberry_price = float(input())
bananas = float(input())
oranges = float(input())
raspberry = float(input())
strawberry = float(input())

money_needed = 0

raspberry_price = strawberry_price / 2
oranges_price = raspberry_price * 0.60
bananas_price = raspberry_price * 0.20

money_needed = strawberry * strawberry_price + \
                bananas * bananas_price + \
                oranges * oranges_price + \
                raspberry * raspberry_price



print(f'{money_needed:.2f}')