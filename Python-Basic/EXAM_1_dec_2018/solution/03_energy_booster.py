fruit = input()
size = input()
count_stek = int(input())

price = 0
if fruit == 'Watermelon':
    if size == 'small':
        price = 56.00 * 2
    if size == 'big':
        price = 28.70 * 5
if fruit == 'Mango':
    if size == 'small':
        price = 36.66 * 2
    if size == 'big':
        price = 19.60 * 5
if fruit == 'Pineapple':
    if size == 'small':
        price = 42.10 * 2
    if size == 'big':
        price = 24.80 * 5
if fruit == 'Raspberry':
    if size == 'small':
        price = 20.00 * 2
    if size == 'big':
        price = 15.20 * 5

end_price = count_stek * price
if 400 <= end_price <= 1000:
    end_price = end_price - (end_price * 0.15)
if end_price > 1000:
    end_price = end_price - (end_price * 0.50)
print(f'{end_price:.2f} lv.')
