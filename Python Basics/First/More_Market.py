vegetables_price = float(input())
fruits_price = float(input())
total_killos_vegetables = int(input())
total_killos_fruits = int(input())

incom_money = \
    vegetables_price * total_killos_vegetables +\
    fruits_price * total_killos_fruits \

incom_euro = incom_money / 1.94

print (f"{incom_euro:.2f}")


