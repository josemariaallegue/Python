import re


def limpiador(texto: str, remplazar=" ") -> str:

    longitudTexto = len(texto)

    for i in range(longitudTexto):

        for caracter in remplazar:

            if(caracter in [".", "^", "$", "*", "+", "?", "{", "}", "[", "]", "\\", "\|", "(", ")"]):
                caracter = "\\" + caracter

            reObjeto = re.compile(r"^" + caracter)
            texto = reObjeto.sub("", texto)
            reObjeto = re.compile(caracter + r"$")
            texto = reObjeto.sub("", texto)

    return texto


texto = "....,,,,,rrttgg.....banana....rrr...."
patron = ",.grt"
print(limpiador(texto, patron))
print(texto.strip(patron))
