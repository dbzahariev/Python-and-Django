c_1 = input()
c_2 = input()
result = float(input())

USD = 1.79549
EUR = 1.95583
GBP = 2.53405


if c_2 == "EUR":
    result /= EUR
    c_2 = "BGN"

if c_2 == "USD":
    result /= USD
    c_2 = "BGN"

if c_2 == "GBP":
    result /= GBP
    c_2 = "BGN"

if c_2 == "BGN":
    if c_1 == "USD":
        result *= USD
    if c_1 == "EUR":
        result *= EUR
    if c_1 == "GBP":
        result *= GBP

print(round(result, 2))
