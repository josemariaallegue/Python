print("in y not in operadores")
lista = [1,2,3,4,5]
print(1 in lista)
print(6 in lista)
print(6 not in lista)
print("")

print("The Multiple Assignment Trick")
cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size + " " + color + " " + disposition)

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size + " " + color + " " + disposition)
print("")

print("Funcion enumerate()")
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies): # devuelve el index y el item separados
    print('Index ' + str(index) + ' in supplies is: ' + item)