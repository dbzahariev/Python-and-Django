text = input()

days = 1
all_km = 5364  # bazov Lager
while True:
    if text.upper() == "END":
        print(f'Failed!\n{all_km}')
        break
    night = text.lower()
    km = int(input())
    if night == "yes":
        days += 1
    if days <= 5:
        all_km += km

    if all_km >= 8848:
        print(f'Goal reached for {days} days!')
        break
    if days > 5:
        print(f'Failed!\n{all_km}')
        break
    text = input()
