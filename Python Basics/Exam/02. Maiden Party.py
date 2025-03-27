LOVE_MESSAGE_PRICE = 0.60
ROSE_PRICE = 7.20
KEYHOLDER_PRICE = 3.60
PAINTING_PRICE = 18.20
SURPRISE_PRICE = 22


party_price = float(input())
love_messages = int(input())
roses = int(input())
keyholders = int(input())
paintings = int(input())
surprises = int(input())



total_messages_price = love_messages * LOVE_MESSAGE_PRICE
total_roses_price = roses * ROSE_PRICE
total_keyholders_price = keyholders * KEYHOLDER_PRICE
total_paintings_price = paintings * PAINTING_PRICE
total_surprises_price = surprises * SURPRISE_PRICE

total_pieces = love_messages + roses + keyholders + paintings + surprises

total_money = total_surprises_price + total_paintings_price + total_keyholders_price + total_roses_price + total_messages_price

if total_pieces >= 25:
    total_money *= 0.65

hosting_cost = total_money * 0.10

final_money = total_money - hosting_cost

if final_money >= party_price:
    print(f"Yes! {final_money - party_price:.2f} lv left.")
else:
    print(f"Not enough money! {party_price - final_money:.2f} lv needed.")



