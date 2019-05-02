import math

count_sectors = float(input())
capaciti = float(input())
price_ticket = float(input())

total_income = capaciti * price_ticket
income_sector = total_income / count_sectors
money_for_charity = (total_income - (income_sector * 0.75)) / 8

# total_income
print(f'Total income - {total_income:.2f} BGN')
print(f'Money for charity - {money_for_charity:.2f} BGN')