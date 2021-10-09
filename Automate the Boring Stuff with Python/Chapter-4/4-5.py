print("Tuples")
tupla = (1,2,3,4)
print(tupla)
print("")

print("iguales a las listas pero son inmutables")
try:
    tupla[1] = 3
except:
    print("error")
print("")
print("sirven para tener listas de elementos que no pretendemos modificar")