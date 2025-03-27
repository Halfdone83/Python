day_of_week = input()
output = ''

if day_of_week == 'Monday':
    output = 'Working day'
elif day_of_week == 'Tuesday':
    output = 'Working day'
elif day_of_week == 'Wednesday':
    output = 'Working day'
elif day_of_week == 'Thursday':
    output = 'Working day'
elif day_of_week == 'Friday':
    output = 'Working day'
elif day_of_week == 'Saturday':
    output = 'Weekend'
elif day_of_week == 'Sunday':
    output = 'Weekend'
else:
    output = 'Error'

print(output)