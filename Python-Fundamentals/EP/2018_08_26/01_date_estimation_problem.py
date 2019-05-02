from datetime import date

data = list(map(int, input().split('-')))
# data = list(map(int, '2018-08-26'.split('-')))

a = date(data[0], data[1], data[2])
b = date(2018, 8, 26)
days_between = (a - b).days

if days_between == 0:
    print('Today date')
elif days_between < 0:
    print('Passed')
else:
    days_between += 1
    print(f'{days_between} days left')
