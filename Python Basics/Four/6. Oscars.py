actor = input()
academy_points = float(input())
judges = int(input())

total_points = academy_points

for i in range(judges):
    judge_name = input()
    judge_points = float(input())
    points_given = len(judge_name) * judge_points / 2
    total_points += points_given

    if total_points >= 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f'Sorry, {actor} you need { 1250.5 - total_points:.1f} more!')