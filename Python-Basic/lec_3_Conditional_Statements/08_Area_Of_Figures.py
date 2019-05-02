import math

figure = input()

area = None
if figure == 'square':
    side = float(input())
    area = side * side
elif figure == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
elif figure == 'circle':
    side = float(input())
    area = math.pi * side * side
elif figure == 'triangle':
    side_1 = float(input())
    side_2 = float(input())
    area = (side_1 * side_2) / 2

area = round(area, 3)
print(area)
