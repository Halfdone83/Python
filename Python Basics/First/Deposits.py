
deposit = float(input())
deposit_term = int(input())
yearly_int = float(input()) / 100

sum = deposit  + deposit_term * ((deposit * yearly_int ) / 12)

print (sum)

