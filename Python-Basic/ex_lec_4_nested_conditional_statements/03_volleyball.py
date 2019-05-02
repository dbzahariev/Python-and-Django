import math
is_leap = input()
p = float(input())
h = float(input())

weekend_days = (48.0 - h) * 3/4
holidays = p * 2/3
all_games = weekend_days + holidays + h
result = math.floor(all_games)
if is_leap == "leap":
    result = math.floor(all_games * 1.15)
print(result)
