price_otivane = float(input())
price_vryshtane = float(input())
price_one_match = float(input())
count_match = int(input())
otstypka = int(input())

count_friends = 6

all_sum = (count_friends * (price_otivane + price_vryshtane))
all_sum = all_sum * (1 - (otstypka / 100))
all_match = count_match * price_one_match * count_friends
all_sum += all_match

print(f'Total sum: {all_sum:.2f} lv.')
print(f'Each friend has to pay {all_sum / count_friends:.2f} lv.')
