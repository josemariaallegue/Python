import os
import Modules
from pathlib import Path
import pyinputplus as pyip
from instaloader.instaloader import Instaloader


def main():

    l = Instaloader()
    pathGeneral = Path(r"E:\Imagenes\Instagram")
    pathResumenes = Path(r"E:\Imagenes\Resumenes")
    pathPerfiles = Path(r"E:\Imagenes\Conseguir")
    archivoPerfiles = "Instagram.txt"
    ultimoUpdate = Modules.preparcionInicial(
        pathResumenes, ["Resumen borrado.txt", "Resumen guardado.txt", "Ultimo update.txt"])
    os.chdir(r"E:\Imagenes\Instagram")

    try:
        if(pyip.inputInt("Ingrese 1 para update o 2 para new: ", 1, min=1, max=2,) == 1):
            # l.login(os.environ.get("INSTA_USER"), os.environ.get("INSTA_PASS"))
            Modules.update(l, pathGeneral, ultimoUpdate, pathResumenes)

        else:
            # usuarios
            # l.login(os.environ.get("INSTA_USER"), os.environ.get("INSTA_PASS"))
            Modules.new(l, pathGeneral, pathPerfiles, archivoPerfiles)

    except Exception as e:
        print(f"Error: {str(e)}")

    print("Finish")


if __name__ == "__main__":
    main()

    """ Incoporar: Agregar una comprobacion de que exista el usuario
               Revisar si la carpeta esta creada pero vacia (genera error)
               Listado de usuarios y contraseñas desde archivo txt
               """
