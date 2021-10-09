print("Lista simple, cambio y eliminacion de valores")
lista = [] # lista vacia
lista = [1,2,3]
print(lista)
print(lista[1])
print(lista[-1])
lista[-1] = 4
print(lista[-1])
del lista[-1]
print(lista[-1])
print("")

print("Lista de listas")
lista = [[1,2,3],[4,5,6]]
print(lista[1][2])
print("")

print("Slices de listas")
lista = [1,2,3,4,5,6,7,8,9]
print(lista[1:6])
print(lista[1:-1])
print(lista[:5])
print(lista[5:])
print("")

print("Largo de listas")
print(len(lista))
print("")

print("Concatenacion y multiplicacion de listas")
lista1 = [1,2,3]
lista2 = ["a","b","c"]
print(lista1 + lista2)
print(lista2 * 3)
print("")

print("Muestra de contenido a travez de for")
lista2 = ["a","b","c"]
for item in lista2:
    print(item)

