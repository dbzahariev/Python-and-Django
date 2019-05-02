price = dict(puzzle=2.60, speaking_Doll=3.0, teddy_Bear=4.1, minion=8.2, truck=2.0)

price_Excursion = float(input())
count = dict(puzzle=int(input()), speaking_Doll=int(input()), teddy_Bear=int(input()), minion=int(input()),
             truck=int(input()))

total_sum = count["puzzle"] * price["puzzle"]
total_sum += count["speaking_Doll"] * price["speaking_Doll"]
total_sum += count["teddy_Bear"] * price["teddy_Bear"]
total_sum += count["minion"] * price["minion"]
total_sum += count["truck"] * price["truck"]

count_Toys = 0
for x in count:
    count_Toys += count[x]
if count_Toys >= 50:
    total_sum *= 0.75
rent = total_sum / 10
profit = total_sum - rent
money_left = profit - price_Excursion
if money_left < 0:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")
else:
    print(f"Yes! {money_left:.2f} lv left.")
