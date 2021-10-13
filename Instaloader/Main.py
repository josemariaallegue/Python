import os
import Modules
from instaloader.instaloader import Instaloader

l = Instaloader()
pathGeneral = r"E:\Imagenes\Instagram"
pathResumenes = r"E:\Imagenes\Resumenes"
pathPerfiles = r"E:\Imagenes\Conseguir"
archivoPerfiles = "Instagram.txt"

# usuarios
# l.login("jasonspeed123", "henryford1992") a verificar
#l.login("howyoudoing1098020", "henryford1992")

os.chdir(r"E:\Imagenes\Instagram")

ultimoUpdate = Modules.preparcionInicial(
    pathResumenes, ["Resumen borrado.txt", "Resumen guardado.txt", "Ultimo update.txt"])

#Modules.new(l, pathGeneral, pathPerfiles, archivoPerfiles)
Modules.update(l, pathGeneral, ultimoUpdate, pathResumenes)


print("Finish")

""" Incoporar: Agregar una comprobacion de que exista el usuario
               Revisar si la carpeta esta creada pero vacia (genera error)
               Listado de usuarios y contraseñas desde archivo txt
               """
