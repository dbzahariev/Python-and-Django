budget = float(input())
season = input()
fisherman = float(input())

price_boat = None
if season == "Spring":
    price_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
else:  # season == "Winter"
    price_boat = 2600

discount = None
if fisherman <= 6:
    discount = 10
elif 7 <= fisherman <= 11:
    discount = 15
else:
    discount = 25

if fisherman % 2 == 0 and season != "Autumn":
    discount += 5

price = price_boat - ((discount / 100) * price_boat)

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - price):.2f} leva.")
