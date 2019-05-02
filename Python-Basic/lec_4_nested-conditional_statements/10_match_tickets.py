budget = float(input())
category = input()
count_people = float(input())

for_transport_percent = None
for_tickets = None
all_price = None
if 1 <= count_people <= 4:
    for_transport_percent = 75
elif 5 <= count_people <= 9:
    for_transport_percent = 60
elif 10 <= count_people <= 24:
    for_transport_percent = 50
elif 25 <= count_people <= 49:
    for_transport_percent = 40
elif count_people > 50:
    for_transport_percent = 25
budget -= ((budget * for_transport_percent) / 100)
if category == 'Normal':
    for_tickets = 249.99
else:
    for_tickets = 499.99
for_tickets = for_tickets * count_people
if budget >= for_tickets:
    print(f"Yes! You have {(budget - for_tickets):.2F} leva left.")
else:
    print(f"Not enough money! You need {(for_tickets - budget):.2F} leva.")
