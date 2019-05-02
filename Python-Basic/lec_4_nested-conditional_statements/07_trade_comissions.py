city = input().lower()
sales = float(input())

commission_rate = -1
if 0 <= sales <= 500:
    if city == 'sofia':
        commission_rate = 5
    elif city == 'varna':
        commission_rate = 4.5
    elif city == 'plovdiv':
        commission_rate = 5.5
elif 500 < sales <= 1000:
    if city == 'sofia':
        commission_rate = 7
    elif city == 'varna':
        commission_rate = 7.5
    elif city == 'plovdiv':
        commission_rate = 8
elif 1000 < sales <= 10000:
    if city == 'sofia':
        commission_rate = 8
    elif city == 'varna':
        commission_rate = 10
    elif city == 'plovdiv':
        commission_rate = 12
elif sales > 10000:
    if city == 'sofia':
        commission_rate = 12
    elif city == 'varna':
        commission_rate = 13
    elif city == 'plovdiv':
        commission_rate = 14.5

if commission_rate == -1:
    print('error')
else:
    commission = (sales * commission_rate) / 100
    print(f"{commission:.2f}")
