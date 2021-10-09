import copy

print("Evitar copiar una lista como reeferencia a un espacio en memoria")
lista = [1,2,3,4]
lista2 = copy.copy(lista)

print(id(lista))
print(id(lista2))
print("")

lista = [[1,2,3],[4,5,6]]
lista2 = copy.deepcopy(lista) # cuando hay listas dentro de listas
