N1 = int(input())
N2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = N1 + N2
elif operator == "-":
    result = N1 - N2
elif operator == "*":
    result = N1 * N2
elif operator == "/" and N2 != 0:
    result = N1 / N2
elif operator == "%" and N2 != 0:
    result = N1 % N2

even_odd_result = "even" if result % 2 == 0 else "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{N1} {operator} {N2} = {result} - {even_odd_result}")

elif operator == "/":
    if N2 == 0:
        print(f" Cannot divide {N1} by zero")
    else:
        print(f" {N1} / {N2} = {result:.2f}")

elif operator == "%":
    if N2 == 0:
        print(f" Cannot divide {N1} by zero")
    else:
        print(f" {N1} % {N2} = {result}")

