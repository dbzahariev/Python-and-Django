x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())

is_in_x = (x_3 >= x_1) and (x_3 <= x_2)
is_in_y = (y_3 >= y_1) and (y_3 <= y_2)

if is_in_x and is_in_y:
    print('Inside')
else:
    print('Outside')
