from math import ceil

serial_name = str(input())
episode_length = int(input())
brake_length = int(input())

lunch_time = brake_length / 8
rest_time = brake_length / 4

total_time = episode_length + lunch_time + rest_time

if total_time <= brake_length:
    print(f"You have enough time to watch {serial_name} and left with {ceil (brake_length - total_time)} minutes free time.")

else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(total_time - brake_length)} more minutes.")