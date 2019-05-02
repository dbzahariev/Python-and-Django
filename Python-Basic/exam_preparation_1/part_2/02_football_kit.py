price_Tshirt = float(input())
budget = float(input())

price_short = price_Tshirt * 0.75
price_chorapi = price_short * 0.20
price_butonki = (price_Tshirt + price_short) * 2
all_sum = price_Tshirt + price_short + price_chorapi + price_butonki
all_sum = all_sum * 0.85
# budget -= all_sum
# print(all_sum)
if all_sum >= budget:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {all_sum:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {(budget - all_sum):.2f} lv. more.')
