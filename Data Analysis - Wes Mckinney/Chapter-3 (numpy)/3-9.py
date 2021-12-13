import numpy as np

print("Universal Functions: Fast Element-Wise Array Functions")

# A universal function, or ufunc, is a function that performs element-wise operations on data in ndarrays
data = np.arange(10)
print(data)
print()

# square root
print(np.sqrt(data))
print()

# exponencial
print(np.exp(data))
print()

# maximun devuelve el elemento maximo entre 2 arrays (deben tener la misma cantidad)
arr = np.random.randn(9)
arr2 = np.random.randn(8)

print(np.maximum(arr, arr2))
print()


# existen un monton de funciones
