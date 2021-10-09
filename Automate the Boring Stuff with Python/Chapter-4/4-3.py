import random

print("Funciones random.choice() y random.shuffle() ")
animales = ["perro", "gato", "caballo", "pajaro", "araña", "pescado", "sapo"]
print(random.choice(animales)) # devuelve un item random

random.shuffle(animales) # mescla la ubicacion de los items
for item in animales:
    print(item)
print("")

print("Metodo index(), append(), insert(), remove(), sort(), reverse()")
lista = [1,2,3,4,5,4]
print(lista.index(4)) # devuelve la primer coincidencia

lista.append(6)
for item in lista:
    print(item,end="")
print("")

lista.insert(1,200)
for item in lista:
    print(item,end="")
print("")

lista.remove(4)
for item in lista:
    print(item,end="")
print("")

lista.sort()
for item in lista:
    print(item,end="")
print("")

lista.sort(reverse=True)
for item in lista:
    print(item,end="")
print("")

lista.reverse()
for item in lista:
    print(item,end="")
print("")