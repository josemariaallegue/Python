import numpy as np

print("Sorting")

data = np.random.randn(10)

print(data)
print()

data.sort()  # al igual que las listas
print(data)
print()

data2 = np.random.randn(5, 3)

print(data2)
print()

data2.sort(0)
print(data2)
print()

data2.sort(1)
print(data2)
