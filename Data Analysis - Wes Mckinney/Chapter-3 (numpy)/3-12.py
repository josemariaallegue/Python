import numpy as np

print("Methods for Boolean Arrays")

data = np.random.randn(100)
# como true = 1 y false = 0 la suma permite contar cantidad de verdaderos
print((data > 0).sum())
print()

bools = np.array([False, False, True, False])
print(bools.any())  # devuelve true si hay por lo menos un verdadero
print()
print(bools.all())  # devuelve true si todos son verdadero
print()
# estas 2 funciones sirven tambien para otro tipos de array. Cualquier valor distinto a 0 se considera como verdadero
