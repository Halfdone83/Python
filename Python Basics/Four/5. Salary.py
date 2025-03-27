tabs = int(input())
salary = int(input())

fine = 0

for _ in range(tabs):
    site = input()
    if site == 'Facebook':
        fine += 150
    elif site == 'Instagram':
        fine += 100
    elif site == 'Reddit':
        fine += 50

    if fine >= salary:
        print("You have lost your salary.")
        break

else:
    print(f"{salary - fine}")