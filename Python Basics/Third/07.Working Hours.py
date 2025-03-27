hour = int(input())
day = input()
result = ""

if day == "Monday" and 10 <= hour <= 18:
    result = 'open'
elif day == "Tuesday" and 10 <= hour <= 18:
    result = 'open'
elif day == "Wednesday" and 10 <= hour <= 18:
    result = 'open'
elif day == "Thursday" and 10 <= hour <= 18:
    result = 'open'
elif day == "Friday" and 10 <= hour <= 18:
    result = 'open'
elif day == "Saturday" and 10 <= hour <= 18:
    result = 'open'

else:
    result = 'closed'

print(result)