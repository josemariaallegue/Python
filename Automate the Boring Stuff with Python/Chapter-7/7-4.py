import re
# {} estable cuantas veces se tiene que repetir un patron
print(r"Expresiones regulares - {}")
reObjeto = re.compile(r"(HA){3}")
mo = reObjeto.search("HAHA")
try:
    print(mo.group())
except:
    print("none")

# si se ponen numero separados por coma se establece un minimo y un maximo
# si alguno de los 2 se deja vacio es que no tiene limites para arriba o para abajo
reObjeto = re.compile(r"(HA){2,3}")
mo = reObjeto.search("HAHAHAHA")
try:
    print(mo.group())
except:
    print("none")
print("")

print(r"Expresiones regulares - greedy o lazy")
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

# el ? establece que se tiene que tomar la menor cantiad de repeticiones posibles de las establecidas
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
