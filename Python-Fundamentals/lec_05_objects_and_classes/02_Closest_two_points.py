import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(p_1, p_2):
    side_a = abs(p_1.x - p_2.x)
    side_b = abs(p_1.y - p_2.y)
    distance = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
    return distance


count_row = int(input())
all_point = []
for i in range(count_row):
    data = input().split(' ')
    x = int(data[0])
    y = int(data[1])
    p = Point(x, y)
    all_point.append(p)

distance_dict = {}
for i_1 in range(len(all_point)):
    for i_2 in range(len(all_point)):
        if i_1 == i_2:
            break
        p_2 = all_point[i_1]
        p_1 = all_point[i_2]
        distance = calc_distance(p_1, p_2)
        if distance not in distance_dict:
            distance_dict[distance] = [[p_1.x, p_1.y], [p_2.x, p_2.y]]
        else:
            distance_dict[distance].extend([[p_1.x, p_1.y], [p_2.x, p_2.y]])

for key in sorted(distance_dict):
    print(f'{key:.3f}')
    print(f'({distance_dict[key][0][0]}, {distance_dict[key][0][1]})')
    print(f'({distance_dict[key][1][0]}, {distance_dict[key][1][1]})')
    break

print(f'{31.00:.12g}')
print(f'{3.0:.12f}')
print(round(3.1))
