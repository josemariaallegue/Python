import numpy as np

print("Basic Indexing and Slicing\n")

# en arrays unidimensionales
arr = np.arange(10)
print(arr)
print()
print(arr[5])
print()
print(arr[5:])
print()
print(arr[1:3])
print()

# al hacer un slice se devuelve la referencia por lo que una modificacion
# en un slice implica la modificacion en el original
arrSlice = arr[1:5]
arrSlice[1] = 12000
print(arr)
print()

# para copiar un array se hace

arrSlice2 = arr[5:8].copy()
print(arrSlice2)
print()

# asi se agarra todos los elementos
arrSlice[:] = 12000
print(arr)
print()

# arrays multi dimensionales
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [7, 8, 9]])
print(arr3d[1])
print()
print(arr3d[0][0][0])
print()
print(arr3d[0][1][1:3])
