import math

name_team = input()
budget = float(input())
count_beer = int(input())
count_chips = int(input())

price_all_beer = 1.20 * count_beer # 1.20 is price beer
price_one_chips = price_all_beer * 0.45
price_all_chips = math.ceil(price_one_chips * count_chips)
all_price = price_all_beer + price_all_chips
budget -= all_price

if budget >= 0:
    print(f"{name_team} bought a snack and has {budget:.2f} leva left.")
else:
    print(f"{name_team} needs {abs(budget):.2f} more leva!")
