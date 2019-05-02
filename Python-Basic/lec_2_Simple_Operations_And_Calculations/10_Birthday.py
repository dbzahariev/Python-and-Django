length = int(input())
width = int(input())
height = int(input())
percent = float(input())

liters = ((length * width * height) * 0.001) * (1 - (percent * 0.01))
print(f"{liters:.3f}")
