MENS_PRICE = 15
LADY_PRICE = 20
KIDS_PRICE = 10
MAINTENANCE_PRICE = 20
COLOUR_PRICE = 30

target = int(input())

money_earned = 0

while True:
    user_input = input()
    if user_input == 'closed':
        break

    if user_input == 'haircut':
        service = input()
        if service == 'mens':
            money_earned += MENS_PRICE
        elif service == 'ladies':
            money_earned += LADY_PRICE
        elif service == 'kids':
            money_earned += KIDS_PRICE
    elif user_input == 'color':
        service = input()
        if service == 'touch up':
            money_earned +=MAINTENANCE_PRICE
        else:
            money_earned +=COLOUR_PRICE

    if money_earned >= target:
        print("You have reached your target for the day!")
        break
if money_earned < target:
    print(f"Target not reached! You need {target - money_earned}lv. more.")

print(f"Earned money: {money_earned}lv.")