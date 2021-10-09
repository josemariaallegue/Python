import re
print("Expresiones regulares - *")
# * esteblece que un patron se puede repetir o no infinata numeros de veces
reObjeto = re.compile(r"Bat(wo)*man")
mo = reObjeto.search("The adventures of Batman")
print(mo.group())

mo = reObjeto.search("The adventures of Batwoman")
print(mo.group())

mo = reObjeto.search("The adventures of Batwowowowowowoman")
print(mo.group())
print("")

print("Expresiones regulares - +")
# igular a * pero tienen que haber como minimo una ocurrencia del patro
reObjeto = re.compile(r"Bat(wo)+man")
mo = reObjeto.search("The adventures of Batman")
if(mo == None):
    print("none")
else:
    print(mo.group())

mo = reObjeto.search("The adventures of Batwoman")
print(mo.group())

mo = reObjeto.search("The adventures of Batwowowowowowoman")
print(mo.group())
print("")
