months = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_other_bills = 0

for i in range(months):
    electricity_bill = float(input())
    water_bill = 20
    internet_bill = 15
    other_bills = (electricity_bill + water_bill + internet_bill) * 1.20

    total_electricity += electricity_bill
    total_water += water_bill
    total_internet += internet_bill
    total_other_bills += other_bills

all_bills = total_other_bills + total_internet + total_electricity + total_water

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other_bills:.2f} lv")
print(f"Average: {all_bills / months:.2f} lv")




