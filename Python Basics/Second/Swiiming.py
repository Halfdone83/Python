record_time = float(input())
distance = float(input())
time_for_meter = float(input())


water_resistance = distance // 15 * 12.5

total_time = distance * time_for_meter + water_resistance

if total_time < record_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f" No, he failed! He was {abs(total_time - record_time):.2f} seconds slower.")
