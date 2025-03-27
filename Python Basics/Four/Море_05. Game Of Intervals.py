moves = int(input())

from_0_9 = 0
from_10_19 = 0
from_20_29 = 0
from_30_39 = 0
from_40_50 = 0
invalid_numbers = 0

total_result = 0

for _ in range(moves):
    numbers = int(input())
    if numbers < 0:
        invalid_numbers += 1
        total_result /= 2

    elif numbers <= 9:
        from_0_9 += 1
        total_result += numbers * 0.20

    elif numbers <= 19:
        from_10_19 += 1
        total_result += numbers * 0.30

    elif numbers <= 29:
        from_20_29 += 1
        total_result += numbers * 0.40

    elif numbers <= 39:
        from_30_39 += 1
        total_result += 50

    elif numbers <= 50:
        from_40_50 += 1
        total_result += 100
    else:
        invalid_numbers += 1
        total_result /= 2

print(f'{total_result:.2f}')
print(f"From 0 to 9: {from_0_9 / moves * 100:.2f}%")
print(f"From 10 to 19: {from_10_19 / moves * 100:.2f}%")
print(f"From 20 to 29: {from_20_29 / moves * 100:.2f}%")
print(f"From 30 to 39: {from_30_39 / moves * 100:.2f}%")
print(f"From 40 to 50: {from_40_50 / moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / moves * 100:.2f}%")
