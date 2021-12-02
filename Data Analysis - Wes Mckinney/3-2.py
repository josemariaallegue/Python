import numpy as np

print("Varios methods of numpy\n")

# crea un array de solamente ceros con 10 elemtnos
data1 = np.zeros(10)

# crea un array de solamente vacios con 10 elemtnos
data2 = np.empty(10)

# para crear con varias dimensiones se pasa una tupla
data3 = np.zeros((2, 2, 3))
print(data3)

# arange es la version de range en numpy
data4 = np.arange(15)
print(data4)
