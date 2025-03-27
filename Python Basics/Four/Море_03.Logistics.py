courses = int(input())


price = 0

bus_tones = 0
truck_tones = 0
train_tones = 0


for i in range(courses):
    weight = int(input())

    if weight <= 3:
        price += 200 * weight
        bus_tones += weight

    elif weight <= 11:
        price += 175 * weight
        truck_tones += weight

    else:
        price += 120 * weight
        train_tones += weight

total_weight = bus_tones + train_tones + truck_tones

print(f' {price / total_weight:.2f}')
print(f' {bus_tones / total_weight * 100:.2f}%')
print(f" {truck_tones / total_weight * 100:.2f}%")
print(f'{train_tones / total_weight * 100:.2f}%')