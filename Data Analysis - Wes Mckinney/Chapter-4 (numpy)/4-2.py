import numpy as np

print("Expressing Conditional Logic as Array Operations")

# np.where es como hacer un if-else pero con arrays
# es mucho mas rapido que con un for
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# el primero y segundo parametro pueden no ser arrays
print(np.where(cond, xarr, yarr))
print()

data = np.random.randn(4, 4)
data2 = data > 0

print(data)
print()
print(data2)
print()
# se pueden remplazar los datos con 2 resultados distintos
print(np.where(data2, 2, -2))
print()
# se pueden replazar alguno de los 2 datos con valores distintos o dejarlo igual
print(np.where(data2, 2, data))
