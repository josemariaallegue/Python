import datetime
import time

print("Datetime")

# momento actual
print(datetime.datetime.now())

# creacion de un objeto datetime determinado y obtencion de sus datos
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(f"{dt.year} {dt.month} {dt.day} {dt.hour} {dt.minute} {dt.second}")

# creacion de objeto datetime desde time.time
print(datetime.datetime.fromtimestamp(10000))
print(datetime.datetime.fromtimestamp(time.time()))

# comparacion de datetime
dt1 = datetime.datetime.now()
dt2 = datetime.datetime.now()
print(dt1 < dt2)
print(dt1 == dt2)
