number = int(input())
result = ''

valid_number = 100 <= number <= 200 or number == 0

if not valid_number:
    result = 'invalid'

print(result)
