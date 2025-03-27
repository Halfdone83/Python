student_name = input()
fails = 0
grade = 1
average_score = 0

while True:
    score = float(input())
    if score < 4:
        fails += 1
        if fails >= 2:
            print(f"{student_name} has been excluded at {grade} grade")
            break

    if score >= 4:
        grade += 1

    average_score += score
    if grade > 12:
        break
if fails < 2:
    print(f"{student_name} graduated. Average grade: {average_score / 12:.2f}")
