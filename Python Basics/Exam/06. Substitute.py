K = int(input())
L = int(input())
M = int(input())
N = int(input())

changes = 0

for first in range(K, 8 + 1):
    for second in range(9, L - 1, -1):
        for first_2 in range(M, 8 + 1):
            for second_2 in range(9, N - 1, -1):
                if first % 2 == 0 and second % 2 != 0 and first_2 % 2 == 0 and second_2 % 2 != 0:
                    if first == first_2 and second == second_2:
                        print("Cannot change the same player.")
                    else:
                        print(f'{first}{second} - {first_2}{second_2}')
                        changes += 1

                if changes >= 6:
                    exit()


