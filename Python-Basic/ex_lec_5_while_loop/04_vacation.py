target_money = float(input())
have_money = float(input())
count_spend_days = 0
count_all_days = 0
while True:
    doing = input()
    money = float(input())
    count_all_days += 1
    if doing == "spend":
        have_money -= money
        if have_money < 0:
            have_money = 0
        count_spend_days += 1
    else:
        count_spend_days = 0
        have_money += money

    if count_spend_days == 5:
        print(f"You can't save the money.")
        print(f"{count_all_days}")
        break
    if have_money >= target_money:
        print(f"You saved the money for {count_all_days} days.")
        break
