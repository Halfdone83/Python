x = float(input())
y = float(input())
h = float(input())

front_and_rear_wall = 2 * (x * x) - (1.2 * 2)
side_wall = 2 * (x * y) - 2 * (1.5 * 1.5)
roof = 2 * (x * y) + 2 * ((x * h)/2)

green_paint = (front_and_rear_wall + side_wall) / 3.4
red_paint = roof / 4.3

print (f"{green_paint:.2f}")
print(f"{red_paint:.2f}")

