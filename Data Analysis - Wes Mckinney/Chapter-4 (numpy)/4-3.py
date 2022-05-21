import numpy as np

print("Mathematical and Statistical Methods")

data = np.random.randn(5, 4)
print(data)
print()
print(data.sum())  # suma de todos los valores
print()
print(data.sum(1))  # suma de las columnas devuelve
print()
print(data.sum(0))  # sumas de las filas
print()
print(data.mean())  # mean aritmetico
print()
print(data.prod())  # producto
print()


data2 = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# suma acumulada. Tambien se puede hacer por columnas o filas
print(data2.cumsum())
print()

data3 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(data3)
print()
# en mas de una dimension cumsum parece que invierte? las columna y filas
print(data3.cumsum(1))
print()
print(data3.cumsum(0))
