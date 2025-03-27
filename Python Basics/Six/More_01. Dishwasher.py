BOTTLE = 750
SOAP_FOR_DISHES = 5
SOAP_FOR_POTS = 15

bottles = int(input())

total_deterget = bottles * BOTTLE
total_deterget_needed = 0

total_dishes = 0
total_pots = 0

load_count = 0

while total_deterget_needed < total_deterget:
    user_input = input()
    if user_input == "End":
        print("Detergent was enough!")
        print(f"{total_dishes} dishes and {total_pots} pots were washed.")
        print(f"Leftover detergent {total_deterget - total_deterget_needed} ml.")
        break

    number_of_dishes = int(user_input)

    load_count += 1

    if load_count % 3 == 0:
        total_pots += number_of_dishes
    else:
        total_dishes += number_of_dishes

    dishes_detergent = total_dishes * SOAP_FOR_DISHES
    pot_detergent = total_pots * SOAP_FOR_POTS

    total_deterget_needed = dishes_detergent + pot_detergent

else:
    print(f"Not enough detergent, {total_deterget_needed - total_deterget} ml. more necessary!")
