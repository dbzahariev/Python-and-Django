class Rectangle:
    def __init__(self, Left, Top, Width, Height):
        self.Left = Left
        self.Top = Top
        self.Width = Width
        self.Height = Height

        self.Right = self.Left + self.Width
        self.Bottom = self.Top + self.Height


data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))
rect_1 = Rectangle(data_1[0], data_1[1], data_1[2], data_1[3])
rect_2 = Rectangle(data_2[0], data_2[1], data_2[2], data_2[3])


def is_inside(r1, r2):
    return r1.Left >= r2.Left and r1.Right <= r2.Right and r1.Top <= r2.Top and r1.Bottom <= r2.Bottom


if is_inside(rect_1, rect_2):
    print('Inside')
else:
    print('Not inside')
