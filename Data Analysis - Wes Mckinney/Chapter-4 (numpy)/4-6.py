import numpy as np

print("Unique and Other Set Logic")

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

print(np.unique(names))  # array con los valores unicos

values = np.array([6, 0, 0, 3, 2, 5, 6])

# verifica si los contenidos de un array estan dentro de otro
print(np.in1d(values, [6, 2]))
