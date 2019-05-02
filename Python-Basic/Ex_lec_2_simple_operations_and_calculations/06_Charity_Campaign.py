days_charity = int(input())
baker_count = int(input())
cake_count = int(input())
waffle_count = int(input())
pancake_count = int(input())

cake = 45
waffle = 5.80
pancake = 3.20

total_cake_price = cake_count * cake
total_waffle_price = waffle_count * waffle
total_pancake_price = pancake_count * pancake
total_money_day = (total_pancake_price + total_waffle_price + total_cake_price) * baker_count
total_money_charity = total_money_day * days_charity
money_after_costs = total_money_charity - (total_money_charity / 8)

print(f"{money_after_costs:.2f}")
