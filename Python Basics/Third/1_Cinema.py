projection_type = input()
rows = int(input())
columns = int(input())

income = 0


if projection_type == "Premiere":
    income = rows * columns * 12

elif projection_type == 'Normal':
    income = rows * columns * 7.50

elif projection_type == 'Discount':
    income = rows * columns * 5

print (f'{income:.2f}')
