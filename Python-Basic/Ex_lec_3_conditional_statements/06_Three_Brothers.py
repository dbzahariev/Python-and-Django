import math

brother_1 = float(input())
brother_2 = float(input())
brother_3 = float(input())
fish = float(input())

cleaning_time = 1 / (1 / brother_1 + 1 / brother_2 + 1 / brother_3)
cleaning_time = cleaning_time * 0.15 + cleaning_time
time_left = fish - cleaning_time

time_left = math.floor(time_left)
print(f"Cleaning time: {cleaning_time:.2f}")

if time_left >= 0:
    print(f"Yes, there is a surprise - time left -> {time_left} hours.")
else:
    print(f"No, there isn't a surprise - shortage of time -> {abs(time_left)} hours.")
