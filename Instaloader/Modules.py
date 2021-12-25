import os
import datetime
import re
import send2trash
import shutil
from glob import glob
from pathlib import Path
from instaloader.structures import Profile
from instaloader.instaloader import Instaloader


def new(l: Instaloader, pathGeneral: str, pathPerfiles: str, archivoPerfiles: str):
    """descargar todos los post de un perfil de un listado de perfiles desde cero
       o continua una que no se haya terminado


    Args:
        l (Instaloader): la instancia instaloader
        pathGeneral (str): la ruta con todos los perfiles descargados
        pathPerfiles (str): la ruta con el listado de perfiles
        archivoPerfiles (str): el nombre del archivo con el listado
    """
    for perfil in cargarPerfiles(pathPerfiles, archivoPerfiles):

        perfil = str(perfil).rstrip("\n")
        pathFull = Path(pathGeneral, perfil)
        profileAux = Profile.from_username(l.context, perfil)

        # revisa si el perfil se ha descargado con anterioridad
        # si es verdadero busca el ultimo archivo descargado y descarga desde el siguiente
        # si es falso descarga desde cero
        if (os.path.exists(pathFull)):

            # busco el archivo con la fecha mas antigua
            # para saber desde que fecha hay que descargar
            for folder, subfolders, files in os.walk(pathFull):

                subfolders.sort()
                pathAux = Path(folder, subfolders[0])
                break

            files = [file for file in glob(
                str(pathAux)+r"\*") if Path(file).is_file()]
            files.sort(key=os.path.getmtime)

            lastDateFinal = re.search(r'(\d+-\d+-\d+)', files[0]).group()

            flag = False
            # establesco donde se descargaran los achivos
            os.chdir(pathGeneral)

            for post in profileAux.get_posts():

                # descargo el posto solamente si encuentro el ultimo descargado
                if (flag):
                    l.download_post(post, perfil)

                elif (datetime.datetime.strptime(
                        lastDateFinal, "%Y-%m-%d").date() == post.date.date()):
                    flag = True

        else:

            for post in profileAux.get_posts():

                l.download_post(post, perfil)

        # limpieza general
        cleaning(str(Path(pathGeneral, perfil)), ".txt")
        cleaning(str(Path(pathGeneral, perfil)), ".xz")
        cleaning2(str(Path(pathGeneral, perfil)))
        ordenamientoAño(str(Path(pathGeneral, perfil)))
        eliminarPerfil(pathPerfiles, archivoPerfiles)


def update(l: Instaloader, pathGeneral: str, ultimoUpdate: str, pathResumenes: str):
    """actualizado los perfiles descargados con los post nuevos desde la fecha
       de ultima actualizacion

    Args:
        l (Instaloader): la instacia de instaloader
        pathGeneral (str): la ruta con todos los perfiles descargados y a actualizar
        ultimoUpdate (str): la fecha de ultima actualizacion
        pathResumenes (str): la ruta con los archivos de resumenes
    """

    # recorre las carpetas de la ruta y la actualiza los perfiles
    for folder in os.listdir(pathGeneral):

        profileAux = Profile.from_username(l.context, folder)

        for post in profileAux.get_posts():

            if (datetime.datetime.strptime(
                    ultimoUpdate, r"%y-%m-%d_%H-%M-%S") >= post.date_utc):
                break
            else:
                l.download_post(post, folder)

        # limpieza general
        cleaning(str(Path(pathGeneral, folder)), ".txt")
        cleaning(str(Path(pathGeneral, folder)), ".xz")
        cleaning2(str(Path(pathGeneral, folder)))
        ordenamientoAño(str(Path(pathGeneral, folder)))

    preparcionFinal(pathResumenes)


def cleaning(path: str, format: str):
    """Elimina los archivos con cierta extension de una ruta

    Args:
        path (str): la ruta con los archivos
        format (str): la extension de los archivos
    """
    pathAux1 = Path(path)

    for file in pathAux1.glob("*" + format):
        os.unlink(file)


def cleaning2(path: str):
    """Elimina los thumbnails de los videos de una ruta

    Args:
        path (str): la ruta de la carpeta con los archivos a eliminar
    """
    contador = 0

    # ordena los archivos por fecha
    files = [file for file in glob(str(path)+r"\*") if Path(file).is_file()]
    files.sort(key=os.path.getmtime)

    # se guarda en un .txt los nombres de los archivos borrados
    with open(r"E:\Imagenes\Resumenes\Resumen borrado.txt", "a") as resumen:

        # nombre del usuario
        resumen.write(f"Usuario {str(path).split(os.sep)[-1]}\n")

        for i, file in enumerate(files):

            if(Path(file).stem == Path(files[i-1]).stem and len(files) >= 2 and
               Path(files[i-1]).suffix == ".jpg"):

                resumen.write(f"Se elimino el archivo {files[i-1]}\n")
                contador += 1
                send2trash.send2trash(files[i-1])
                del files[i-1]

        resumen.write(f"Un total de {contador} archivos\n\n")


def ordenamientoAño(path: str):
    """Mueve los archivos de una ruta a una subcarpeta correspondiente al año.
        Si no existe la mencionada subcarpeta, se crea

    Args:
        path (str): la ruta de la carpeta con los archivos a mover
    """

    # obtecion de los paths de los archivos y no subcarpetas
    files = [file for file in glob(str(path)+r"\*") if Path(file).is_file()]

    if(len(files) != 0):

        # busqueda de ultimo año y primer año
        files.sort(key=os.path.getmtime)

        primerAño = datetime.datetime.fromtimestamp(
            os.stat(files[0]).st_mtime, tz=datetime.timezone.utc).year

        ultimoAño = datetime.datetime.fromtimestamp(
            os.stat(files[-1]).st_mtime, tz=datetime.timezone.utc).year

        # creacion de carpetas
        for i in range(primerAño, ultimoAño + 1):
            if(not Path(path, str(i)).is_dir()):
                Path.mkdir(Path(path, str(i)))

        for file in files:
            añoFile = datetime.datetime.fromtimestamp(
                os.stat(file).st_mtime, tz=datetime.timezone.utc).year
            if(not Path(Path(path, str(añoFile), Path(file).name)).is_file()):
                shutil.move(file, Path(path, str(añoFile)))
            else:
                send2trash.send2trash(file)


def preparcionFinal(path: str):
    """guarda la fecha de ultima actualizacion en un archivo

    Args:
        path (str): la ruta con el archivo
    """
    with open(Path(path, "Ultimo update.txt"), "w") as fileAux:
        fileAux.write(
            str(datetime.datetime.utcnow().strftime(r"%y-%m-%d_%H-%M-%S")))


def preparcionInicial(path: str, archivos: list) -> str:
    """Limpieza de los .txt con los resumenes y
    obtencion de la fecha del ultimo update

    Args:
        path (str): ubicacion de los archivos
        archivos (list): listado de archivos a limpiar

    Returns:
        str: [la fecha de la ultima ejecucion]
    """

    fecha = None

    for archivo in archivos:

        if(archivo == "Ultimo update.txt"):
            with open(Path(path, archivo), "r") as fileAux:
                fecha = fileAux.read()
        else:
            with open(Path(path, archivo), "w") as fileAux:
                fileAux.write("")

    return fecha


def cargarPerfiles(path: str, archivo: str) -> list:
    """devuelve el listado de perfiles que todavia no se han descargado o
       que no se termino de descargar

    Args:
        path (str): ruta con el listado de perfiles
        archivo (str): nombre del archivo con el listado

    Returns:
        list: [description]
    """
    pathAux = Path(path, archivo)

    if(pathAux.is_file()):
        with open(Path(path, archivo), "r") as file:
            return file.readlines()


def eliminarPerfil(path: str, archivo: str):
    """elimina un perfil completamente descargado del listado de perfiles

    Args:
        path (str): ruta del listado
        archivo (str): nombre del archivo con el listado
    """
    pathAux = Path(path, archivo)

    # copio los datos
    if(pathAux.is_file()):
        datoAux = cargarPerfiles(path, archivo)
        del datoAux[0]

    # sobreescribo el archivo
    if(pathAux.is_file()):
        with open(Path(path, archivo), "w") as file:
            file.writelines(datoAux)


def pruebas(l: Instaloader, instagramProfile: str):

    user = Profile.from_username(l.context, instagramProfile)
    # for destacadas in l.get_highlights(user):
    l.download_highlights(user)


def pruebas2(usuario: str):

    contador = 0

    for folder, subfolders, files in os.walk(Path(r"")):

        for file in files:
            if str(file).endswith(".mp4"):
                contador += 1

    print(str(contador))
