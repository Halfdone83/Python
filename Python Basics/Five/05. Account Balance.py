
total_sum = 0
user_input = None

while user_input != 'NoMoreMoney':
    user_input = input()
    if user_input == 'NoMoreMoney':
        break

    user_input = float(user_input)
    if user_input < 0:
        print("Invalid operation!")
        break

    total_sum += user_input
    print(f"Increase: {user_input:.2f} ")

print(f'Total: {total_sum:.2f}')