total_number = float(input())
total = 0.0
while not total_number == 0:
    number = float(input())
    if number < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {number:.2f}")
    total += number
    total_number -= 1
print(f"Total: {total:.2f}")
