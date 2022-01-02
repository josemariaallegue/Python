import os
import Modules
from instaloader.instaloader import Instaloader


def main():

    l = Instaloader()
    pathGeneral = r"E:\Imagenes\Instagram"
    pathResumenes = r"E:\Imagenes\Resumenes"
    pathPerfiles = r"E:\Imagenes\Conseguir"
    archivoPerfiles = "Instagram.txt"

    try:
        # usuarios
        # l.login("jasonspeed123", "henryford1992") a verificar
        #l.login("howyoudoing0o9i8u7y6t5r", "qwerty123456")

        os.chdir(r"E:\Imagenes\Instagram")

        ultimoUpdate = Modules.preparcionInicial(
            pathResumenes, ["Resumen borrado.txt", "Resumen guardado.txt", "Ultimo update.txt"])

        #Modules.new(l, pathGeneral, pathPerfiles, archivoPerfiles)
        Modules.update(l, pathGeneral, ultimoUpdate, pathResumenes)

    except Exception as e:
        print(f"Error: {str(e)}")

    print("Finish")


if __name__ == "__main__":
    main()

    """ Incoporar: Agregar una comprobacion de que exista el usuario
               Revisar si la carpeta esta creada pero vacia (genera error)
               Listado de usuarios y contraseñas desde archivo txt
               """
