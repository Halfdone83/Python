numbers = int(input())

OddSum = 0
OddMin = float("inf")
OddMax = float("-inf")
EvenSum = 0
EvenMin = float("inf")
EvenMax = float("-inf")

for _ in range(1, numbers + 1):
    number = float(input())

    if number % 2 == 0:
        EvenSum += number
        EvenMin = min(EvenMin, number)
        EvenMax = max(EvenMax, number)

    else:
        OddSum += number
        OddMin = min(OddMin, number)
        OddMax = max(OddMax, number)

if EvenMin == float("inf") or EvenMax == float("-inf"):
    EvenMin = "No"
    EvenMax = "No"

if OddMin == float("inf") or OddMax == float("-inf"):
    OddMin = "No"
    OddMax = "No"

print(f'OddSum={OddSum:.2f},')
print(f'OddMin={OddMin:.2f},')
print(f'OddMax={OddMax:.2f},')
print(f'EvenSum={EvenSum:.2f},')
print(f'EvenMin={EvenMin:.2f},')
print(f'EvenMax={EvenMax:.2f},')
