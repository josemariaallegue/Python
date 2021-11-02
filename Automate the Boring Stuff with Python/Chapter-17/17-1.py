import time

print("Time")

inicio = time.time()

for i in range(0, 10000000):
    None
print('Took %s seconds to calculate.' % (time.time() - inicio))

# ctime() le da formato al tiempo actual
print(time.ctime())
