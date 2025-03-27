flowers_type = input()
flowers_count = int(input())
budget = int(input())

ROSE_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

result = 0

if flowers_type == "Roses":
    result = ROSE_PRICE * flowers_count

    if flowers_count > 80:
        result *= 0.90

elif flowers_type == "Dahlias":
    result = DAHLIAS_PRICE * flowers_count

    if flowers_count > 90:
        result *= 0.85

elif flowers_type == "Tulips":
    result = TULIPS_PRICE * flowers_count

    if flowers_count > 80:
        result *= 0.85

elif flowers_type == 'Narcissus':
    result = NARCISSUS_PRICE * flowers_count

    if flowers_count < 120:
        result *= 1.15

elif flowers_type == 'Gladiolus':
    result = GLADIOLUS_PRICE * flowers_count

    if flowers_count < 80:
        result *= 1.20


if budget >= result:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {budget - result:.2f} leva left.")
else:
    print(f"Not enough money, you need {result - budget:.2f} leva more.")


