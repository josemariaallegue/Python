import numpy as np

print("Casting data types in arrays\n")

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
print(arr.dtype)
print()

arr2 = arr.astype(np.int64)
print(arr2.dtype)
print(arr2)
