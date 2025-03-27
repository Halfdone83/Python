number = int(input())


for num2 in range(1111, 10_000):
     for digit in str(num2):
         if digit == '0':
             break

         if number % int(digit) != 0:
            break
     else:
         print(num2, end=" ")
