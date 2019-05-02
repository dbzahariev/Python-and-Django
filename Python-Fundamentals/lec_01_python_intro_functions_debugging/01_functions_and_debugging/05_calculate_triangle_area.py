def calc_area(a, b):
    return (a * b) / 2


num_1 = float(input())
num_2 = float(input())

area = calc_area(num_1, num_2)
print(f'{area:.12g}')
