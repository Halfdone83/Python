day_off = int(input())


working_days = 365 - day_off
tom_norm_playtime = 30000
day_off_playtime = 127
working_days_playtime = 63

total_play_time = day_off * 127 + working_days * 63

time_left_to_play = abs(tom_norm_playtime - total_play_time)

hours = time_left_to_play // 60
minutes = time_left_to_play % 60

if total_play_time > tom_norm_playtime:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
