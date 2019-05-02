price = {"Argentina": {"flags": 3.25, "caps": 7.20, "posters": 5.10, "stickers": 1.25},
         "Brazil": {"flags": 4.20, "caps": 8.50, "posters": 5.35, "stickers": 1.20},
         "Croatia": {"flags": 2.75, "caps": 6.90, "posters": 4.95, "stickers": 1.10},
         "Denmark": {"flags": 3.10, "caps": 6.50, "posters": 4.80, "stickers": 0.90}}

team_name = input()
souvenir = input()
count = int(input())
if team_name not in price:
    print("Invalid country!")
elif souvenir not in price[team_name]:
    print("Invalid stock!")
else:
    one_price = price[team_name][souvenir]
    all_price = one_price * count
    print(f"Pepi bought {count} {souvenir} of {team_name} for {all_price:.2f} lv.")
