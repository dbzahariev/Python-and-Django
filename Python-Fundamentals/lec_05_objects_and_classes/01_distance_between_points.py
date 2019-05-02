import math

data_1 = input().split(' ')
data_2 = input().split(' ')

x_1 = int(data_1[0])
y_1 = int(data_1[1])

x_2 = int(data_2[0])
y_2 = int(data_2[1])


class Point:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y


p_1 = Point(x_1, y_1)
p_2 = Point(x_2, y_2)

side_a = abs(p_1.x - p_2.x)
side_b = abs(p_1.y - p_2.y)

distance = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
print(f'{distance:.3f}')
