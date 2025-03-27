first_num = int(input())
last_num = int(input())
magic_num = int(input())


counter = 0
is_found = False

for i in range(first_num , last_num + 1):
    if is_found == True:
        break
    for x in range(first_num , last_num + 1):
        counter += 1
        if x + i == magic_num:
            is_found = True
            print(f"Combination N:{counter} ({i} + {x} = {magic_num})")
            break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_num}")