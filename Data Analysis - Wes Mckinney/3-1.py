import numpy as np

print("Ndarray\n")

# creacion
data = [6, 7.5, 8, 0, 1]
arr = np.array(data)
print(arr)
print()

# creacion de uno multidimensional
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print()

print(arr2.ndim)  # cantidad de dimensiones
print(arr2.shape)  # cantidad de dimensiones y de elemtnos por dimension
print(arr2.dtype)  # tipo de los elementos del array
