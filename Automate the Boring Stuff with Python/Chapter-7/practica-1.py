import re
import datetime


def determinarFecha(fechas: list):

    for fecha in fechas:
        fechaAux = datetime.datetime.strptime(fecha, r"%d/%m/%Y")

        if(isinstance(fechaAux, datetime.date)):
            print(f"{fecha} es fecha")
        else:
            print(f"{fecha} no es fecha")


def obtenerFecha(texto: str):

    reObjeto = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)
    determinarFecha(reObjeto.findall(texto))


obtenerFecha("sssss 19/07/0999 19/07/1000 19/07/2999 19/07/3000")
#reObjeto = re.compile(r"[0-3][0-9]/[0-1][0-9]/[1000-2999]{4}")
#reObjeto = re.compile(r"\d{2}/\d{2}/\d{4}")
#print(reObjeto.findall("sssss 19/07/0999 19/07/2999 19/07/2000 19/07/1000"))
# [0-3][0-9]/[0-1][0-9]/[1000-2999]
