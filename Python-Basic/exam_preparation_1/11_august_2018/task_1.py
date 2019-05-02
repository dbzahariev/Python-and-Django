time_break = int(input())
price_one_part = float(input())
price_program = float(input())
price_frappe = float(input())

time_break -= 5  # time_frappe
time_break -= 6  # time_computer
time_break -= 4  # time_program

all_money = (3 * price_one_part)
all_money += 2 * price_program
all_money += price_frappe
print(f'{all_money:.2f}')
print(f'{time_break}')
