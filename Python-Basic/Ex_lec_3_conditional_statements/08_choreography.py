import math

steps = int(input())
dancers = int(input())
days = int(input())

steps_per_day = math.ceil(((steps / days) / steps) * 100)
dancers_day = (steps_per_day / dancers)

if steps_per_day < 13:
    print(f"Yes, they will succeed in that goal! {dancers_day:.2f}%.")
else:
    print(f"No, They will not succeed in that goal! Required {dancers_day:.2f}% steps to be learned per day.")
