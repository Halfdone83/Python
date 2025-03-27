capacity = int(input())
fans = int(input())

sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for _ in range(fans):
    sector = input()

    if sector == "A":
        sector_A += 1
    elif sector == "B":
        sector_B += 1
    elif sector == "V":
        sector_V += 1
    elif sector == "G":
        sector_G += 1

print(f"{sector_A / fans * 100:.2f}%")
print(f"{sector_B / fans * 100:.2f}%")
print(f"{sector_V / fans * 100:.2f}%")
print(f"{sector_G / fans * 100:.2f}%")
print(f"{fans / capacity * 100:.2f}%")