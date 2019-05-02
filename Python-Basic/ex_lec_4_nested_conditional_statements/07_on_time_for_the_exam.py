hour_start = int(input())
minute_start = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

is_late = ""
hour_difference = hour_arrive - hour_start
minute_difference = minute_arrive - minute_start

if hour_difference >= 0 and minute_difference > 0:
    is_late = "Late"
elif hour_difference == 0 and minute_difference <= 30:
    is_late = "On time"
elif hour_difference <= 0 and minute_difference <= 30:
    is_late = "Early"

print(is_late)

result_hour = ""
result_minute = ""
if hour_difference > 0:
    result_hour = hour_difference
if minute_difference <= 9:
    result_minute = "0:", minute_difference
else:
    result_minute = minute_difference

is_after = ""
if is_late == "Late":
    is_after = "after"
else:
    is_after = "before"

if not (minute_difference == 0 and hour_difference == 0):
    if result_hour != "":
        print(f"{result_hour}:{result_minute} hours {is_after} the start")
    else:
        print(f"{result_minute} minutes {is_after} the start")

# Не работи
