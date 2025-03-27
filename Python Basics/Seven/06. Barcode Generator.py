first_num = int(input())
second_num = int(input())

first_num_4 = first_num % 10
second_num_4 = second_num % 10

first_num = first_num // 10
second_num = second_num // 10

first_num_3 = first_num % 10
second_num_3 = second_num % 10

first_num = first_num // 10
second_num = second_num // 10

first_num_2 = first_num % 10
second_num_2 = second_num % 10

first_num = first_num // 10
second_num = second_num // 10

first_num_1 = first_num
second_num_1 = second_num

for i in range(first_num_1, second_num_1 + 1):
    for j in range(first_num_2, second_num_2 + 1):
        for k in range(first_num_3, second_num_3 + 1):
            for l in range(first_num_4, second_num_4 + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f'{i}{j}{k}{l}', end=' ')