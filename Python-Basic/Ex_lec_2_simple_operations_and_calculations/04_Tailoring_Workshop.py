rectangle_table = int(input())
length_table = float(input())
width_table = float(input())

meters = rectangle_table * (length_table + 2 * 0.30) * (width_table + 2 * 0.30)
meters_2 = rectangle_table * (length_table / 2) * (length_table / 2)
price_dollar = meters * 7 + meters_2 * 9
price_lev = price_dollar * 1.85

print(f"{price_dollar:.2f} USD")
print(f"{price_lev:.2f} BGN")
