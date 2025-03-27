first_player = int(input())
second_player = int(input())

while True:
    user_input = input()
    if user_input == 'End':
        print(f"Player one has {first_player} eggs left.")
        print(f"Player two has {second_player} eggs left.")
        break
    elif user_input == 'one':
        second_player -= 1
    elif user_input == 'two':
        first_player -= 1

    if first_player <= 0:
        print(f"Player one is out of eggs. Player two has {second_player} eggs left.")
        break
    if second_player <= 0:
        print(f"Player two is out of eggs. Player one has {first_player} eggs left.")
        break