skumria_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = palamud_kg * (skumria_price + skumria_price * 0.60)
safrid_price = safrid_kg * (caca_price + caca_price * 0.80)
midi_price = midi_kg * 7.50


total_cost =  \
    palamud_price +\
    safrid_price+\
    midi_price

print(f"{total_cost:.2f}")

