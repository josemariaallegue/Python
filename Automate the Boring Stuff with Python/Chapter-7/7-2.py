import re
# es como un or devuelve la primer ocurreciancia de un grupo de patrones
print("Expresiones regulares - pipe")
reObjeto = re.compile(r"Batman|Robin")
mo = reObjeto.search("Batman and Robin")
print(mo.group())
mo = reObjeto.search("Robin and Batman")
print(mo.group())
print("")

# patrones que comienzan con Bat y terminan con alguna de las 4 opciones entre parentesis
# solo trae la primer ocurrencia
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel and Batcopter lost a window.')
print(mo.group())
print(mo.group(1))
print("")

print("Expresiones regulares - ?")
# ? determina que una parte del patron es opcional. Esto evitar errores.
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# ? establece que los primeros digitos del numero son opcionales
phoneNumRegex = re.compile(r'((\(\d\d\d)\)-)?(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 555-4242.')
print(mo.group())
phoneNumRegex = re.compile(r'((\(\d\d\d)\))?-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (123)-555-4242.')
print(mo.group())
