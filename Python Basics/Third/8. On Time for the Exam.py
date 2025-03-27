exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())


exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

time_difference = exam_time - arrival_time

if time_difference > 30:
    print("Early")

elif time_difference < 0:
    print("Late")

else:
    print("On time")

hours = abs(time_difference) // 60
minutes = abs(time_difference) % 60

