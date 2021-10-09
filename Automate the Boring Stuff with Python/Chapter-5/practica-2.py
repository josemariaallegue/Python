import random

def cargarInventario(inventario: dict, item: str, cantidad:int):
    
    inventario[item.lower()] = cantidad

    return None

def mostrarInventario(inventario:dict):
    
    print("Inventory")
    contador = 0
    for key, item in inventario.items():
        print(str(key) + " " + str(item))
        contador += item
    
    print("Total number of items: " + str(contador))

    return None

inventario = {}
items = ["rope", "torch", "dager", "arrow", "bow", "sword"]

for item in items:
    cargarInventario(inventario, item, random.randint(1, 25))

mostrarInventario(inventario)
