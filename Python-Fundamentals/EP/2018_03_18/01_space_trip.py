star = input()
distance_gm = int(input())
budget = int(input())
fuel_consumption_for_100_gm = float(input())
gas_price_for_1_liter = float(input())

liter_per_gm = fuel_consumption_for_100_gm / 100
price_per_gm = liter_per_gm * gas_price_for_1_liter
total_price = distance_gm * price_per_gm
leftover = budget - total_price
if leftover >= 0:
    print(f'Off to {star} with ${leftover:.2f} for snacks')
else:
    print(f'Maybe another time, need ${abs(leftover):.2f} more')
