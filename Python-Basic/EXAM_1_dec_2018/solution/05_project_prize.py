parts = int(input())
awards_for_points = float(input())

all_points = 0
for i in range(1, parts + 1):
    points_for_part = int(input())
    if i % 2 == 0:
        points_for_part *= 2
    all_points += points_for_part

result = all_points * awards_for_points
print(f'The project prize was {result:.2f} lv.')
