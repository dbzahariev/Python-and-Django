import math


class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


class Box:
    def __init__(self, UpperLeft, UpperRight, BottomLeft, BottomRight):
        self.UpperLeft = UpperLeft
        self.UpperRight = UpperRight
        self.BottomLeft = BottomLeft
        self.BottomRight = BottomRight

        self.Width = calculate_distance(points[0], points[1])
        self.Height = calculate_distance(points[0], points[2])
        self.Perimeter = 2 * self.Width + 2 * self.Height
        self.Area = self.Width * self.Height

    def __str__(self):
        return f'Box: {self.Width:.12g}, {self.Height:.12g}\nPerimeter: {self.Perimeter:.12g}\nArea: {self.Area:.12g}'


def calculate_distance(point1, point2):
    side_a = abs(point1.X - point2.X)
    side_b = abs(point1.Y - point2.Y)

    distance = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
    return distance


data = input()
boxes = []
while not data == 'end':
    data = data.split(' | ')
    points = []
    for point in data:
        X_and_Y = list(map(int, point.split(':')))
        one_point = Point(X_and_Y[0], X_and_Y[1])
        points.append(one_point)

    one_box = Box(points[0], points[1], points[2], points[3])
    boxes.append(one_box)
    data = input()

for box in boxes:
    print(box)
