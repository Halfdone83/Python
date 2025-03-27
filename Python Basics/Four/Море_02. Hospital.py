period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period + 1):
    patients = int(input())

    if day % 3 ==0 and untreated_patients > treated_patients:
        doctors += 1

    treated_today = min(doctors, patients)
    untreated_today = patients - treated_today

    treated_patients += treated_today
    untreated_patients += untreated_today

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
