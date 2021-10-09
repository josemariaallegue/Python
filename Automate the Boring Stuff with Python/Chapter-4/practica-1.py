def modulo(lista: list) -> str:

    texto= ""

    for i, item in enumerate(lista):

        if(i == len(lista)-1):
            texto += " and "
        elif(i >= 1):
            texto += ", "

        texto += str(item)

    return texto


lista = [1,2,3,4,5]
print(modulo(lista))
