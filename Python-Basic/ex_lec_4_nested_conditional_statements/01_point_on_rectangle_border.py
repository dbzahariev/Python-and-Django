x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())

is_in_x = ((x_3 == x_1) or (x_3 == x_2)) and (y_1 <= y_3 <= y_2)
is_in_y = ((y_3 == y_1) or (y_3 == y_2)) and (x_1 <= x_3 <= x_2)

if is_in_x or is_in_y:
    print('Border')
else:
    print('Inside / Outside')
