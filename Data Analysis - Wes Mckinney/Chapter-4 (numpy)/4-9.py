import numpy as np

print("Arithmetic with NumPy Arrays\n")

# arrays son utiles porque permiten modificar el contenido sin hacer un for
arr = np.array([[1., 2., 3.], [4., 5., 6.]])

print(arr * arr)
print()
print(arr + arr)
print()
print(arr - arr)
print()
print(arr * 100)
print()
print(arr ** 2)
print()

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2 > arr)
