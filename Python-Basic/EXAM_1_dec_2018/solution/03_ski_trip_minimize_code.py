count_days = int(input()) - 1  # broi noshtuvki
type_room = input().lower()
rating = input().lower()

sett = {"room  for  one  person": [18.00, 0, 0, 0], "apartment": [25.00, 30, 35, 50], "president apartment": [35.00, 10, 15, 20]}[type_room]
discount = sett[1] if count_days < 10 else sett[2] if count_days >= 10 and count_days <= 15 else sett[3]
price = sett[0] * count_days
price = price - ((price * discount) / 100)
price = price + ((price * 25) / 100) if rating == "positive" else price - ((price * 10) / 100)
print(f'{price:.2f}')
