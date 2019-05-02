import math
hall_length = float(input())
hall_width = float(input())
side_square_wardrobe = float(input())

hall_area = (hall_length * 100) * (hall_width * 100)
wardrobe_area = (side_square_wardrobe * 100) * (side_square_wardrobe * 100)
bench_area = hall_area / 10
free_space = hall_area - wardrobe_area - bench_area
dancer_number = free_space / (40 + 7000)

print(math.floor(dancer_number))
