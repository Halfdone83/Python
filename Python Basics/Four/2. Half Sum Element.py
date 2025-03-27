n = int(input())

biggest_num = 0
total = 0

for _ in range(n):
    temp_num = int(input())
    total += temp_num

    if biggest_num < temp_num:
        biggest_num = temp_num

result = total - biggest_num

if biggest_num == result:
    print('Yes')
    print(f' Sum = {biggest_num}')
else:
    print('No')
    print(f' Diff = {abs(biggest_num - result)}')


