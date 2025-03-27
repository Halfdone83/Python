fruit = input()
day = input()
qty = float(input())

result = 'error'

if day == "Monday" or \
     day == 'Tuesday' or \
     day == 'Wednesday' or \
     day == 'Thursday' or \
     day == 'Friday':
    if fruit == 'banana':
        result = 2.50 * qty
    elif fruit == 'apple':
        result = 1.20 * qty
    elif fruit == 'orange':
        result = 0.85 * qty
    elif fruit == 'grapefruit':
        result = 1.45 * qty
    elif fruit == 'kiwi':
        result = 2.70 * qty
    elif fruit == 'pineapple':
        result = 5.50 * qty
    elif fruit == 'grapes':
        result = 3.85 * qty
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        result = 2.70 * qty
    elif fruit == 'apple':
        result = 1.25 * qty
    elif fruit == 'orange':
        result = 0.90 * qty
    elif fruit == 'grapefruit':
        result = 1.60 * qty 
    elif fruit == 'kiwi':
        result = 3.00 * qty
    elif fruit == 'pineapple':
        result = 5.60 * qty
    elif fruit == 'grapes':
        result = 4.20 * qty

if result == 'error':
    print(result)

else:
    print(f"{result:.2f}")
