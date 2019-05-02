budget = int(input())
count_items = int(input())

items = {"hoodie": 30, "keychain": 4, "t-shirt": 20, "flag": 15, "sticker": 1}
for i in range(0, count_items):
    budget -= items[input().lower()]

if budget >= 0:
    print(f"You bought {count_items} items and left with {budget} lv.")
else:
    print(f"Not enough money, you need {abs(budget)} more lv.")
