import time
import datetime

print("Pausing until a specific date")

now = datetime.datetime.now()
after = now + datetime.timedelta(0, 10)
difference = after-now

print(str(difference.total_seconds()))
time.sleep(difference.total_seconds())
