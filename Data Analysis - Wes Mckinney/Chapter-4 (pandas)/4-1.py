import pandas as pd
import numpy as np

print("Series\n")

"""A Series is a one-dimensional array-like object containing a sequence of values (of
similar types to NumPy types) and an associated array of data labels, called its index"""

data = pd.Series([1, 5, -1, -5, 0])  # creacion
print(data)
print()
print(data.values)  # imprime solo valores
print()
print(data.index)  # imprime informacion del index
print()

# creacion con un index determinado
data2 = pd.Series(data.values, index=['f', 'd', 'b', 'a', 'c'])
print(data2)
print()

print(data2["f"])  # obtencion de un solo valor
print()

data2["f"] = 200  # modificacion de un valor
print(data2["f"])
print()

print(data2[["f", "d"]])  # obtencion de varios valores
print()


print("Operacion varias\n")

print(data2 * 10)
print()
print(data2 > 2)
print()
print(data2[data2 > 2])
print()
print(np.exp(data2))
print()
print(pd.isnull(data2))
print()
print("f" in data2)  # una serie es similar a un diccionario
print()
# se pueden sumar 2 series sin que tengan la misma cantidad de elementos sin importar el orden
# si los elementos no se encuentran en ambas series tirar NaN
print(data + data2)

# se pueden crear series a partir de diccionarios
# se puede elegir el orden de los index si se pasan estos como un parametro en la creacion
data3 = pd.Series({'Ohio': 35000, 'Texas': 71000,
                  'Oregon': 16000, 'Utah': 5000})
print(data3)
print()

# se pueden establecer el nombre la serie y el index
data3.name = "population"
data3.index.name = "state"
print(data3)
