product = input()
day = input()
quantity = float(input())

price_week = {"banana": "2.50", "apple": "1.20", "orange": "0.85", "grapefruit": "1.45", "kiwi": "2.70",
              "pineapple": "5.50", "grapes": "3.85"}
price_weekend = {"banana": "2.70", "apple": "1.25", "orange": "0.90", "grapefruit": "1.60", "kiwi": "3.00",
                 "pineapple": "5.60", "grapes": "4.20"}
week = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
weekend = {"Saturday", "Sunday"}

price_aa = None
if day in week and price_week.get(product) is not None:
    price_aa = float(price_week[product]) * quantity
if day in weekend and price_weekend.get(product) is not None:
    price_aa = float(price_weekend[product]) * quantity

if price_aa is None:
    print('error')
else:
    print(f"{price_aa:.2f}")
