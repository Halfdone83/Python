flowers_type = input()
flowers_count = int(input())
budget = int(input())

ROSE_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

result = None

if flowers_type == "Roses" and flowers_count > 80:
    ROSE_PRICE *= 0.90
    result = ROSE_PRICE * flowers_count

elif flowers_type == "Dahlias" and flowers_count > 90:
    DAHLIAS_PRICE *= 0.85
    result = DAHLIAS_PRICE * flowers_count

elif flowers_type == "Tulips" and flowers_count > 80:
    TULIPS_PRICE *= 0.85
    result = TULIPS_PRICE * flowers_count

elif flowers_type == 'Narcissus' and flowers_count < 120:
    NARCISSUS_PRICE *= 1.15
    result = NARCISSUS_PRICE * flowers_count

elif flowers_type == 'Gladiolus' and flowers_count < 80:
    GLADIOLUS_PRICE *= 1.20
    result = GLADIOLUS_PRICE * flowers_count

if budget > result:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {budget - result:.2f} leva left.")
else:
    print(f"Not enough money, you need {result - budget:.2f} leva more.")
