students = int(input())

top_students = 0
between_4_5 = 0
between_3_4 = 0
fail = 0
total_scores = 0

for i in range(students):
    score = float(input())

    if score <= 2.99:
        total_scores += score
        fail += 1
    elif score <= 3.99:
        total_scores += score
        between_3_4 += 1
    elif score <= 4.99:
        total_scores += score
        between_4_5 += 1
    else:
        total_scores += score
        top_students += 1

print(f'Top students: {top_students / students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {between_4_5 / students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {between_3_4 / students * 100:.2f}%')
print(f'Fail: {fail / students * 100:.2f}%')
print(f'Average: {total_scores / students:.2f}')
