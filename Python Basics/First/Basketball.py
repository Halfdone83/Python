annual_fee = int(input())

shoes = annual_fee  - annual_fee * 0.40
clothes = shoes - shoes * 0.20
ball = clothes / 4
accesoaries = ball / 5

total_price = annual_fee + shoes + clothes + ball + accesoaries

print(total_price)