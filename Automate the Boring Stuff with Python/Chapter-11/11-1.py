from os import path
import traceback
from pathlib import Path

print("Debugging - try, exception and raise exception")
""" Se pueden crear exceptions con raise Exception(texto) y luego 
captarlar con try/except Exception as err"""


def modulo1(flag: bool):
    if(flag):
        raise Exception("Error")
    else:
        print("No hubo error")


try:
    modulo1(True)
except Exception as err:
    print('An exception happened: ' + str(err))

"""When Python encounters an error, it produces a treasure trove of error information called the traceback. 
The traceback includes the error message, the line number of the line that caused the error, 
and the sequence of the function calls that led to the error. This sequence of calls is called the call stack."""
# con tracebak podemos obtener esta informacion

try:
    raise Exception("Error 2")
except:
    path = Path(
        r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-11")
    errorFile = open(Path(path, 'errorInfo.txt'), 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
