size = int(input()) * int(input())  # width * length
while True:
    taking_parts = input()
    if taking_parts == "STOP":
        print(f"{size:.0f} pieces are left.")
        break
    size -= int(taking_parts)
    if size < 0:
        print(f"No more cake left! You need {abs(size):.0f} pieces more.")
        break
