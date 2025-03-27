length = int(input())
height = int(input())
width = int(input())

percent_filled = float(input()) / 100

volume = length * height * width / 1000

final_volume = volume  - volume * percent_filled

print (final_volume)