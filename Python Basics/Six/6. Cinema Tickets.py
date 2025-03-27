
students_tickets = 0
standart_tickets = 0
kids_tickets = 0
total_tickets = 0


while True:
    movie_name = input()

    current_tickets = 0

    if movie_name == "Finish":
        break

    capacity = int(input())

    while current_tickets < capacity:
        ticket = input()

        if ticket == "End":
            break

        if ticket == "student":
            students_tickets += 1
        elif ticket == "standard":
            standart_tickets += 1
        elif ticket == "kid":
            kids_tickets += 1

        current_tickets +=1

    print(f"{movie_name} - {current_tickets / capacity * 100:.2f}% full.")


    total_tickets = students_tickets + standart_tickets + kids_tickets

print(f"Total tickets: {total_tickets}")
print(f"{students_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standart_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")