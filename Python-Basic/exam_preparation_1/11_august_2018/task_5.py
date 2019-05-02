broi_kompiutri = int(input())

all_seils = 0
all_ratings = 0
for i in range(0, broi_kompiutri):
    comp_number = int(input())
    rating = comp_number % 10  # vzimam poslednata cifra
    all_ratings += rating  # dobavqm retinga kym obstata suma
    count_sail = comp_number // 10  # vzimam ostanalite cifri

    percent = -1  # namiram procenta
    if rating == 2:
        percent = 0
    if rating == 3:
        percent = 50
    if rating == 4:
        percent = 70
    if rating == 5:
        percent = 85
    if rating == 6:
        percent = 100

    this_seil = (count_sail * percent) / 100  # namiram kolko prodajbi sa napraveni spored procenta
    all_seils += this_seil  # dobavqm prodajbite kym sbora

print(f'{all_seils:.2f}')  # printiram v nujniq format
print(f'{(all_ratings / broi_kompiutri):.2f}')  # printiram v nujniq format
