
judges = int(input())


total_grades = 0
total_presentations = 0

while True:
    presentation_name = input()

    if presentation_name == 'Finish':
        print(f"Student's final assessment is {total_grades / total_presentations:.2f}.")
        break

    current_grades = 0
    current_presentations = 0

    for _ in range(judges):
        grade = float(input())

        current_grades += grade
        current_presentations += 1

    print(f"{presentation_name} - {current_grades / current_presentations:.2f}.")

    total_grades += current_grades
    total_presentations += current_presentations



