count_pencil = int(input())
count_markers = int(input())
count_preparat = float(input())
procent = int(input())  # cqlo chislo 20

price_pencil = count_pencil * 5.80
price_markers = count_markers * 7.20
price_preparat = count_preparat * 1.20
price_all = price_markers + price_pencil + price_preparat
price_all = price_all - ((price_all * procent) / 100)

print(f'{price_all:.3f}')  # do 3 chislo
