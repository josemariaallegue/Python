import datetime

# creacion de variable tipo delta
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

thousandDays = datetime.timedelta(days=1000)
dt = datetime.datetime.now()

print(dt)
print(dt + thousandDays)
print(dt - thousandDays)
print(dt + (2 * thousandDays))
