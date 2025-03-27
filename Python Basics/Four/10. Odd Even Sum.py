user_input = int(input())

odd_sum = 0
even_sum = 0

for i in range(user_input):
    temp_num = int(input())
    if i % 2 == 0:
        even_sum += temp_num
    else:
        odd_sum += temp_num

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')