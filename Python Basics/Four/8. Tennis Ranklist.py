from math import floor

tournaments = int(input())
starting_points = int(input())

W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720

total_points = 0
won_tournaments = 0

for i in range(tournaments):
    position = input()
    if position == "W":
        total_points += W_POINTS
        won_tournaments += 1
    elif position == "F":
        total_points += F_POINTS
    elif position == "SF":
        total_points += SF_POINTS

print(f'Final points: {total_points + starting_points}')
print(f'Average points: {floor(total_points / tournaments)}')
print(f'{won_tournaments / tournaments * 100:.2f}%')