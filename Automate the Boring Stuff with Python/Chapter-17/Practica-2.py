import time
import winsound

print("It's the final countdown...")
for i in range(60, 0, -1):
    print(f"T minus {i}")
    time.sleep(1)

winsound.Beep(1000, 1000)
