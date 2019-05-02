x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

side_1 = max(x1, x2) - min(x1, x2)
side_2 = max(y1, y2) - min(y1, y2)
area = side_1 * side_2
perimeter = 2 * (side_2 + side_1)
print(area)
print(perimeter)
