groups = int(input())

musala_group = 0
monblan_group = 0
kilimandjaro_group = 0
k2_group = 0
everest_group = 0

total_tourists = 0

for i in range(groups):
    tourists = int(input())
    if tourists <= 5:
        musala_group += tourists
    elif tourists <= 12:
        monblan_group += tourists
    elif tourists <= 25:
        kilimandjaro_group += tourists
    elif tourists <= 40:
        k2_group += tourists
    else:
        everest_group += tourists

    total_tourists = everest_group + k2_group + kilimandjaro_group + monblan_group + musala_group

print(f'{(musala_group / total_tourists)* 100:.2f}%')
print(f'{(monblan_group / total_tourists) * 100:.2f}%')
print(f'{(kilimandjaro_group / total_tourists) * 100:.2f}%')
print(f'{(k2_group / total_tourists) * 100:.2f}%')
print(f'{(everest_group / total_tourists) * 100:.2f}%')