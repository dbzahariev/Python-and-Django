day_in = int(input())
day_in -= 1
day_out = "Error"
all_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
try:
    if day_in >= 0:
        day_out = all_days[day_in]
except IndexError:
    day_out = "Error"
print(day_out)
