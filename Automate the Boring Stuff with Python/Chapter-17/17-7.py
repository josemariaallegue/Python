import threading
import time

print("Threading")


def naping(seconds: int):
    time.sleep(5)
    print("Wake up!")
    print("Second thread finish")


threadObj = threading.Thread(target=naping, args=[5])
threadObj.start()

print("First thread finish")
