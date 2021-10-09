import random
from typing import ItemsView

def  modulo()-> list:

    lista = ["T", "H"]
    listaResultados = []

    for i in range(100):

        listaResultados.append(random.choice(lista))

    return listaResultados

streaks = 0

for i in range(1000):

    listaAux = modulo()
    repeticion = 0

    for j, item in enumerate(listaAux):

        if(item == listaAux[j-1]):
            repeticion += 1
        else:
            if(repeticion >= 6):
                streaks += 1
            repeticion = 0

print("Hay " + str(streaks) + " rachas de 6 iguales")
            







