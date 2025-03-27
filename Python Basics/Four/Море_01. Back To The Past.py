legacy = float(input())
year = int(input())

year_return = 1800

money_spend = 0

for i in range(year_return, year + 1):
    if i % 2 ==0:
        money_spend += 12000
    else:
        money_spend += 12000 + 50 * (18 + i - year_return)

if money_spend <= legacy:
    print(f"Yes! He will live a carefree life and will have {legacy - money_spend:.2f} dollars left." )
else:
    print(f"He will need {money_spend - legacy:.2f} dollars to survive." )



