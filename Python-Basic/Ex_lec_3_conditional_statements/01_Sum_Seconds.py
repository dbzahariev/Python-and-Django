import datetime
total = datetime.datetime(1, 1, 1)
total += datetime.timedelta(seconds=int(input()))
total += datetime.timedelta(seconds=int(input()))
total += datetime.timedelta(seconds=int(input()))
print(total.strftime('%#M:%S'))
