from pathlib import Path
import pyinputplus as pyinp


print("Mad Libs")


def guardar(path: Path, file: str, responds: dict, text: str):

    pathAux = Path(path)

    for key, value in responds.items():
        text = text.replace(key, value)

    if(pathAux.is_dir()):
        pathAux2 = Path(pathAux, file)
        if(pathAux2.is_file()):
            fileAux = open(pathAux2, mode="a")
            fileAux.write(text)

        else:
            fileAux = open(pathAux2, mode="w")
            fileAux.write(text)

        fileAux.close()


respuestas = {"ADJECTIVE": "",
              "NOUN": "",
              "VERB": "",
              "NOUN2": ""}

path = r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-9"
file = "practica-1.txt"
respuestas["ADJECTIVE"] = pyinp.inputStr("Enter an adjective: ")
respuestas["NOUN"] = pyinp.inputStr("Enter a noun: ")
respuestas["VERB"] = pyinp.inputStr("Enter a verb: ")
respuestas["NOUN2"] = pyinp.inputStr("Enter a noun: ")

text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.\n"

guardar(path, file, respuestas, text)

file = open(Path(path, file), mode="r")
print(file.read())
