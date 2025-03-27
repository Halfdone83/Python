total_money = 0

while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())


    while total_money <= budget:
        save = float(input())
        total_money += save

        if total_money >= budget:
            print(f"Going to {destination}!")
            break