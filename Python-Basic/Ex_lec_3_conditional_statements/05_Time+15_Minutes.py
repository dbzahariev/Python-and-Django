hours = int(input())
minutes = int(input())

minutes += 15
if minutes >= 60:
    hours += 1
    minutes -= 60

if hours >= 24:
    hours -= 24

minutes_str = ""
if minutes < 10:
    minutes_str = "0" + str(minutes)
else:
    minutes_str = minutes

print(f"{hours}:{minutes_str}")
