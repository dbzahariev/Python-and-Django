speed = float(input())
a = ("slow", "average", "fast", "ultra fast", "extremely fast")
coefficient = 0
if speed <= 10:
    coefficient = 0
elif 10 < speed <= 50:
    coefficient = 1
elif 50 < speed <= 150:
    coefficient = 2
elif 150 < speed <= 1000:
    coefficient = 3
else:
    coefficient = 4
print(a[coefficient])
