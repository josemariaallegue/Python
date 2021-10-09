import re


def comparacion(password: str, patron: str) -> bool:

    reObjeto = re.compile(patron)
    mo = reObjeto.search(password)
    try:
        print(mo.group())
    except:
        return False

    return True


def longitud(password: str, minimo: int) -> bool:
    if(len(password) < minimo):
        return False

    return True


password = "henryford1992"
listaPatrones = [r"[A-Z]", r"[a-z]", r"\d"]

for patron in listaPatrones:
    if(not comparacion(password, patron)):
        print("Nos se cumple el patron: " + str(patron))

if(not longitud(password, 8)):
    print("Nos se cumple con el minimo de caracteres: " + str(8))
