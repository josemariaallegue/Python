import numpy as np

print("Fancy indexing\n")

# consiste en indexar un array a traves de otro array
arr = np.arange(32).reshape((8, 4))


# digamos que queremos el primer y quinto elemento
# podriamos hacer
print(arr[0], arr[4])
print()

# pero la forma fancy seria
print(arr[[0, 4]])
print()

# si queremos elementos individuales colocamos otro array separdo por comas
print(arr[[0, 4], [1, 2]])
