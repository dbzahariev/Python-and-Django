import math
seconds = float(input())
meters = float(input())
seconds_meters = float(input())

sum_time = (meters * seconds_meters) + ((math.floor(meters / 15)) * 12.5)

if sum_time < seconds:
    print(f"Yes, he succeeded! The new world record is {sum_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {sum_time - seconds:.2f} seconds slower.")
