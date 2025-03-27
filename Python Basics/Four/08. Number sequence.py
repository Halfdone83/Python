number = int(input())
temp_number = int(input())

max_number = temp_number
min_number = temp_number

for i in range(number - 1):
    temp_number = int(input())
    if temp_number > max_number:
        max_number = temp_number
    if temp_number < min_number:
        min_number = temp_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')