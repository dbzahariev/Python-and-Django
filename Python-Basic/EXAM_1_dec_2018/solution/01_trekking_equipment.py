count_climbers = int(input())
count_carabiners = int(input())
count_towels = int(input())
count_pickeys = int(input())

price_carabiner = 36.00
price_towel = 3.60
price_picelle = 19.80

all_price_one_climber = price_carabiner * count_carabiners
all_price_one_climber += price_towel * count_towels
all_price_one_climber += price_picelle * count_pickeys
all_price_all_climbers = all_price_one_climber * count_climbers
all_price_all_climbers = all_price_all_climbers * 1.20 # DDS

print(f'{all_price_all_climbers:.2f}')