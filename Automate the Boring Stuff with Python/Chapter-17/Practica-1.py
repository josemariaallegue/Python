import time

totalTime = 0
i = 0

try:
    while True:
        start = time.time()
        key = input("Press enter...")
        lap = time.time() - start
        totalTime += lap
        i += 1
        print(f"Lap {i} - se tardo {round(lap,2)} segundos en presionar enter")
        print(f"Total - {round(totalTime,2)} segundos")

except KeyboardInterrupt:
    print("\nSe termino la carrera")
