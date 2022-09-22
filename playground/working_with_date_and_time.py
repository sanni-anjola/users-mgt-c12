from datetime import datetime, timedelta

now = datetime.now()

print(f"{now: %A, %B %d %Y}")
print(now.strftime('%A, %B %d %Y'))

dd = datetime(year=2022, hour=23, day=5, month=2, minute=45)
print(dd)
ddd = datetime.strptime("2022/10/10 10:30", "%Y/%m/%d %H:%M")
print(ddd)

x = ddd + timedelta(days=-10)
print(ddd.day)
print(x.day)
