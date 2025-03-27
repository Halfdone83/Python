from math import  sqrt

prime_numbers = 0
non_prime_numbers = 0

while True:
    user_input = input()

    if user_input == 'stop':
        break

    number = int(user_input)

    if number < 0:
        print('Number is negative.')
        continue

    for number2 in range(2, int(sqrt(number)) + 1):
        if number % number2 == 0:
           non_prime_numbers += number
           break
    else:
        prime_numbers += number

print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")