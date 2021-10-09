import re
print("Expresiones regulares - 3 pasos simples")
# patron de numero de telefono
regexAux = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = regexAux.search('My number is 415-555-4242.')
print(mo.group())
print("")

print("Expresiones regulares - parentesis")
# buscar el numero de telefono pero se puede dividir en grupos el resultado
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print("")

print("Expresiones regulares - groups()")
print(mo.groups())
# con devuelve una lista se puede asignar todos los valores de una tupla
aux1, aux2 = mo.groups()
print(aux1)
print(aux2)
print("")

# si se buscan parentesis se pone \( y \)
phoneNumRegex = re.compile(r'(\(\d\d\d)\)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415)-555-4242.')
print(mo.group())
