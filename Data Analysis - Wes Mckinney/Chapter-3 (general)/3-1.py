print("List, set and dict comprehensions\n")

nombres = ["jose", "maria", "allegue"]
lista = [nombre.upper() for nombre in nombres if len(nombre) == 4]
print(lista)
print("")

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = {numero for numero in numeros if numero % 2 == 0}
print(pares)
print("")

aux = {i: "numero: " + str(i) for i in range(10)}
print(aux)
print()


print("Nested list comprehensions\n")
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

result = [name for names in all_data for name in names
          if name.count('e') >= 2]
print(result)
