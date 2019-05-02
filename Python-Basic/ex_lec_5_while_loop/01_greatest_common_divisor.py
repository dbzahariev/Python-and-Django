a = float(input())
b = float(input())
while not a == b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f"{a:.0f}")
