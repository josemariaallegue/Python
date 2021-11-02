import time

print("Time sleep")

print("Begin")
print("Sleeping for 5 seconds")
inicio = time.time()
time.sleep(5)
print("Finish")
print(f"Sleep for {round( time.time()- inicio, 2)} seconds")
