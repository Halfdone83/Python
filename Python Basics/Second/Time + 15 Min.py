hours = int(input())
minutes = int(input())

final_minutes = minutes + 15
final_hours = hours

if final_minutes >= 60:
    final_minutes = final_minutes - 60
    final_hours = hours + 1

if final_hours >= 24:
    final_hours = final_hours - 24

print(f"{final_hours:}:{final_minutes:02d}")

