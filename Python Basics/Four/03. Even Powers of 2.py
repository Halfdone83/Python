number = int(input())

result = 1

for i in range(0, number + 1,):
    if i % 2 == 0:
        print(result)
    result *= 2