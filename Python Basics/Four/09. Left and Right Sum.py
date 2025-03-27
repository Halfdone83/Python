user_input = int(input())

left_numbers = 0
right_numbers = 0


for i in range(user_input):
    temp_number = int(input())
    left_numbers += temp_number

for i in range(user_input):
    temp_number = int(input())
    right_numbers += temp_number

if left_numbers == right_numbers:
    print(f' Yes, sum = {left_numbers}')
else:
    diff = abs(left_numbers - right_numbers)
    print(f' No, diff = {diff}')