import numpy as np

print("Boolean indexing\n")

# indexas un array con otro array de elementos tipo bool
# ejemplo sin sentido

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4,)

# al hacer lo siguiente names == "Bob" creamos una lista/array de elementos bool
# sera true si aparece Bob
# array([ True, False, False, True, False, False, False], dtype=bool)
# al indexar data con esto le digo que me devuelva solo los elementos que coincidan
# con los true, en este caso el 0 y 3
print(data[names == "Bob"])
print()

# se puede hacer con varias condiciones
print(data[(names == "Bob") | (names == "Will")])
print()

# la condicion se puede aplicar sobre la misma lista
# y tambien aplicar un cambio a todos estos elementos
data[data < 0] = 0
print(data)
print()

data[names != "Bob"] = int(69)
print(data)
