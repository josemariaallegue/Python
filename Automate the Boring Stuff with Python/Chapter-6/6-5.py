print("String metodos - rjus(), ljust(), center()")
texto = "Hola mundo!"
print(texto.rjust(20))
print(texto.ljust(20))
print(texto.center(20))
print(texto.rjust(20, "*"))
print(texto.ljust(20, "*"))
print(texto.center(20, "*"))
print("")


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
