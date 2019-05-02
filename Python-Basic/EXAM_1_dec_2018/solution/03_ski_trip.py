count_days = int(input()) - 1 # broi noshtuvki
type_room = input().lower()
rating = input().lower()

discount = 0
price = 18.00
if type_room == "apartment":
    price = 25.00
    if count_days < 10:
        discount = 30
    elif count_days >= 10 and count_days <= 15:
        discount = 35
    elif count_days > 15:
        discount = 50
elif type_room == "president apartment":
    price = 35.00
    if count_days < 10:
        discount = 10
    elif count_days >= 10 and count_days <= 15:
        discount = 15
    elif count_days > 15:
        discount = 20

price = price * count_days
price = price - ((price * discount) / 100)

if rating == "positive":
    price = price + ((price * 25) / 100)
elif rating == "negative":
    price = price - ((price * 10) / 100)

print(f'{price:.2f}')
