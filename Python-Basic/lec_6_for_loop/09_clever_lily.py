year = int(input())
price = float(input())
toys_price = int(input())
sum_money = 0.0
for i in range(1, year + 1):
    if i % 2 == 0:
        sum_money += i * 5 - 1  # for year 8 add 40 lv and - 1 for brother
    else:
        sum_money += toys_price  # add toys_price
diff = sum_money - price
if diff >= 0:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {abs(diff):.2f}")
