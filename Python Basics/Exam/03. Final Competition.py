dancers = int(input())
points = float(input())
season = input()
place = input()

prize = 0

if season == 'summer':
    if place == 'Bulgaria':
        prize = dancers * points
        prize *= 0.95
    elif place == 'Abroad':
        prize = dancers * points
        prize *= 1.5
        prize *= 0.90
elif season == 'winter':
    if place == 'Bulgaria':
        prize = dancers * points
        prize *= 0.92
    elif place == 'Abroad':
        prize = dancers * points
        prize *= 1.5
        prize *= 0.85

charity = prize * 0.75

dancers_money = prize - charity

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {dancers_money / dancers:.2f}")

