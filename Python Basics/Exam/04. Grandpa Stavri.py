days = int(input())


total_liters = 0
total_degrees = 0
average_degrees = 0

for i in range(1, days + 1):
    liters = float(input())
    degrees = float(input())

    total_liters += liters
    total_degrees += degrees * liters

    average_degrees = total_degrees / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif average_degrees < 42:
    print(f"Super!")
else:
    print("Dilution with distilled water!")