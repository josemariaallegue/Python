import numpy as np

print("Transposing Arrays and Swapping Axes")

# reshape modifica la forma del array y devuelve un view sin copiar
# la multiplicacion entre el primer elemento de reshape y el segundo de coidir con la cantidad de elementos
data = np.arange(15).reshape((3, 5))
print(data)
print()

# la T es un atributo de los array que transpone los datos
print(data.T)
print()

print(np.dot(data.T, data))
print()

data2 = np.arange(16).reshape((2, 2, 4))
print(data2)
print()

print(data2.transpose((1, 0, 2)))
print()
print(data2.swapaxes(1, 2))
